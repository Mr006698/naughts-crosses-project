from os import system, name
from enum import StrEnum
from tabulate import tabulate
from grid import Grid, Player
import string

class ANSI(StrEnum):
  LIGHT_RED = '\033[91m'
  LIGHT_GREEN = '\033[92m'
  LIGHT_BLUE = '\033[94m'
  LIGHT_YELLOW = '\033[93m'
  LIGHT_GREY = '\033[37m'

  RED = '\033[31m'
  GREEN = '\033[32m'
  BLUE = '\033[34m'
  YELLOW = '\033[33m'
  GREY = '\033[90m'

  BLACK = '\033[30m'
  WHITE = '\033[97m'

  STYLE = '\033[0m'


class TextGUI:
  def __init__(self, grid: Grid):
    self._grid = grid
    self._current_colour = ANSI.WHITE
    self._create_indices()
    self._create_players()


  def get_move(self, player: Player) -> str:
    colour = ANSI.GREEN if player == Player.ONE else ANSI.BLUE
    while True:
      res = input(f'{colour}PLAYER {player.name}{ANSI.STYLE} Enter Your Move ({ANSI.RED}Q to quit{ANSI.STYLE}): ').strip().upper()
      if res == 'Q':
        return None
      
      if self._grid.is_valid_move(res):
        return res
        
      else:
        print(f'{ANSI.RED}INVALID MOVE{ANSI.STYLE} Please Try Again Using Grid Coodinates e.g A0 or B1 on an empty cell.')


  def draw(self) -> None:
    print(f'{ANSI.YELLOW}NOUGHTS AND CROSSES{ANSI.STYLE}')
    placed_players = [[self._players[col.value] for col in row] for row in self._grid]
    print(tabulate(placed_players,
                   headers=self._col_index,
                   showindex=self._row_index,
                   tablefmt='rounded_grid',
                   stralign='center'))
    
  
  def print_player_wins(self, player: Player) -> bool:
    colour = ANSI.GREEN if player == Player.ONE else ANSI.BLUE
    res = input(f'{colour}PLAYER {player.name}{ANSI.STYLE} Wins! Type Y to Play Again: ').strip().upper()
    if res == 'Y':
      return True
    
    return False


  def _create_indices(self) -> None:
    self._row_index = self._create_row_names()
    self._col_index = self._create_col_names()

  
  def _create_col_names(self) -> list:
    return [f'{col}' for col in range(self._grid._cols)]
  

  def _create_row_names(self) -> list:
    alpha_list = list(string.ascii_uppercase)
    return [alpha_list[num] for num in range(self._grid._rows)]
  

  def _create_players(self) -> None:
    self._players = [' ',
                    f'{ANSI.GREEN}X{ANSI.STYLE}',
                    f'{ANSI.BLUE}O{ANSI.STYLE}']


  def clear_console(self) -> None:
    # for windows
    if name == 'nt':
        system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        system('clear')

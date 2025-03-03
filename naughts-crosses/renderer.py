from os import system, name
from tabulate import tabulate
import numpy as np
import string

class Renderer:
  def __init__(self, grid):
    self._grid = grid
    self._create_ansi_colour_codes()
    self._create_indices()
    self._create_players()


  def _create_indices(self) -> None:
    self._rows, self._cols = self._grid.shape
    self._row_index = self._create_row_names()
    self._col_index = self._create_col_names()


  def _create_ansi_colour_codes(self) -> None:
    self._dark_green = '\033[32m'
    self._light_green = '\033[92m'
    self._dark_blue = '\033[34m'
    self._light_blue = '\033[94'
    self._dark_grey = '\033[30m'
    self._light_grey = '\033[90m'
    self._reset_styles = '\033[0m'

  
  def _create_col_names(self) -> list:
    return [f'{col}' for col in range(self._cols)]
  

  def _create_row_names(self) -> list:
    alpha_list = list(string.ascii_uppercase)
    return [alpha_list[num] for num in range(self._rows)]
  

  def _create_players(self) -> None:
    self._players = [' ',
                    f'{self._dark_green}X{self._reset_styles}',
                    f'{self._dark_blue}O{self._reset_styles}']


  def draw(self) -> None:
    placed_players = [[self._players[col] for col in row] for row in self._grid]
    print(tabulate(placed_players,
                   headers=self._col_index,
                   showindex=self._row_index,
                   tablefmt='rounded_grid',
                   stralign='center'))


  def clear_console(self) -> None:
    # for windows
    if name == 'nt':
        system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        system('clear')

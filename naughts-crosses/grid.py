import string
from enum import Enum

LEFT = -1
RIGHT = 1
UP = -1
DOWN = 1
CENTRE = 0

class Player(Enum):
  NONE = 0
  ONE = 1
  TWO = 2


class WinState(Enum):
  NONE = 0
  WIN = 1
  DRAW = 2


class Grid:
  def __init__(self, rows: int, cols: int):
    # Create the grid
    self._rows = rows
    self._cols = cols
    self._grid = [[Player.NONE for _ in range(cols)] for _ in range(rows)]
    
    # Create grid references
    self._create_grid_ref()


  def add_player(self, player: Player, pos:str, win_line: int = 3) -> WinState:
    coords = self._grid_ref.get(pos)
    # TODO: If coords add player
    # If not coords throw exception

    return self.add_player_at_loc(player, coords, win_line)
  

  def add_player_at_loc(self, player: Player, loc, win_line: int) -> WinState:
    row, col = loc
    self._grid[row][col] = player

    return self._check_win(player, loc, win_line)
  

  def is_valid_move(self, pos:str) -> bool:
    loc = self._grid_ref.get(pos)
    if loc and self.is_empty_cell(loc):
      return True
    
    return False
  

  def is_empty_cell(self, loc: tuple) -> bool:
    row, col = loc
    return self._grid[row][col] == Player.NONE
  

  def find_empty_cell(self, start: tuple, h_dir: int, v_dir: int) -> tuple:
    return self._find_first(start, v_dir, h_dir)
  

  def clear_grid(self) -> None:
    for row in range(self._rows):
      for col in range(self._cols):
        self._grid[row][col] = Player.NONE

  
  def _check_win(self, player: Player, start: tuple, win_line: int) -> WinState:
    if (self._check_horizontal(player, start, win_line) or
            self._check_vertical(player, start, win_line) or
            self._check_diagonal(player, start, win_line)):
      return WinState.WIN
    
    # if no winners check for empty cells
    if self._check_draw():
      return WinState.DRAW
    
    return WinState.NONE
  

  def _check_draw(self) -> bool:
    # If there are empty cells then it is not a draw
    for row in self._grid:
      if Player.NONE in row:
        return False
      
    return True
  

  def _check_horizontal(self, player: Player, start: tuple, win_line: int) -> bool:
    left_loc = self._find_first(player, start, CENTRE, LEFT)
    right_loc = self._find_first(player, start, CENTRE, DOWN)
    
    return self._count_loc(left_loc[1], right_loc[1], win_line)
  

  def _check_vertical(self, player: Player, start: tuple, win_line: int) -> bool:
    up_loc = self._find_first(player, start, UP, CENTRE)
    down_loc = self._find_first(player, start, DOWN, CENTRE)
    
    return self._count_loc(up_loc[0], down_loc[0], win_line)
  

  def _check_diagonal(self, player: Player, start: tuple, win_line: int) -> bool:
    # Upper left to bottom right diagonal
    ul_loc = self._find_first(player, start, UP, LEFT)
    br_loc = self._find_first(player, start, DOWN, RIGHT)

    # Upper right to bottom left diagonal
    ur_loc = self._find_first(player, start, UP, RIGHT)
    bl_loc = self._find_first(player, start, DOWN, LEFT)

    return self._count_loc(ul_loc[0], br_loc[0], win_line) or self._count_loc(ur_loc[0], bl_loc[0], win_line)
  

  # Count the number of adjacent player locations in the grid and return true if a win line
  def _count_loc(self, loc_a: int, loc_b: int, win_line: int) -> bool:
    row_count = 0
    for _ in range(loc_a, loc_b + 1):
      row_count += 1
    
    if row_count == win_line:
      return True

    return False


  # Find the first position of the player in the grid direction
  def _find_first(self, player: Player, start: tuple, row_dir: int, col_dir: int) -> tuple:
    # Unpack the start position and apply the direction
    row, col = start; row += row_dir; col += col_dir

    # Check that the direction is still in the grid
    if row < 0 or row >= self._rows or col < 0 or col >= self._cols:
      return start
    
    if self._grid[row][col] == player:
      return self._find_first(player, (row, col), row_dir, col_dir)
    
    return start
  

  # Create an alpha numeric index into the grid
  def _create_grid_ref(self) -> list:
    alpha_list = list(string.ascii_uppercase)
    self._grid_ref =  {f'{alpha_list[row]}{col}':(row, col) for row in range(self._rows) for col in range(self._cols)}
  

  def get_grid_ref(self) -> dict:
    return self._grid_ref


  def __iter__(self) -> iter:
    return iter(self._grid)
  
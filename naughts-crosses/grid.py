import numpy as np
import string

from renderer import Renderer

LEFT = -1
RIGHT = 1
UP = -1
DOWN = 1
CENTRE = 0

class Grid:
  def __init__(self, rows: int = 3, cols: int = 3, renderer: int = None):
    self._grid = np.zeros((rows, cols), dtype=int)
    self._rows, self._cols = self._grid.shape
    self._create_grid_ref()

    if not renderer:
      self._renderer = Renderer(self._grid)


  def add_player(self, player: int, pos:str, win_line: int = 3) -> bool:
    # TODO: if out of bounds or place taken throw exception
    coords = self._grid_ref.get(pos)
    row, col = coords
    self._grid[row][col] = player

    return self._check_win(player, coords, win_line)
  

  def find_empty_cell(self, start: tuple, h_dir: int, v_dir: int) -> tuple:
    return self._find_first(start, v_dir, h_dir)

  
  def _check_win(self, player: int, start: tuple, win_line: int) -> bool:
    
    return (self._check_horizontal(player, start, win_line) or
            self._check_vertical(player, start, win_line) or
            self._check_diagonal(player, start, win_line))
  

  def _check_horizontal(self, player: int, start: tuple, win_line: int) -> bool:
    left_loc = self._find_first(player, start, CENTRE, LEFT)
    right_loc = self._find_first(player, start, CENTRE, DOWN)
    
    return self._count_loc(left_loc, right_loc, win_line)
  

  def _check_vertical(self, player: int, start: tuple, win_line: int) -> bool:
    up_loc = self._find_first(player, start, UP, CENTRE)
    down_loc = self._find_first(player, start, DOWN, CENTRE)
    
    return self._count_loc(up_loc, down_loc, win_line)
  

  def _check_diagonal(self, player: int, start: tuple, win_line: int) -> bool:
    # Upper left to bottom right diagonal
    ul_loc = self._find_first(player, start, UP, LEFT)
    br_loc = self._find_first(player, start, DOWN, RIGHT)

    # Upper right to bottom left diagonal
    ur_loc = self._find_first(player, start, UP, RIGHT)
    bl_loc = self._find_first(player, start, DOWN, LEFT)

    return self._count_loc(ul_loc, br_loc, win_line) or self._count_loc(ur_loc, bl_loc, win_line)
  

  # Count the number of adjacent player locations in the grid and return true if a win line
  def _count_loc(self, loc_a: tuple, loc_b: tuple, win_line: int) -> bool:
    row_count = 0
    for _ in range(loc_a[0], loc_b[0]+1):
      row_count += 1
    
    if row_count == win_line:
      return True

    return False


  # Find the first position of the player in the grid direction
  def _find_first(self, player: int, start: tuple, row_dir: int, col_dir: int) -> tuple:
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
    

  def draw_grid(self) -> None:
    #self.clear_console()
    # Column index
    #column_index = [f'{index}' for index in range(self._cols)]
    # img = '    ' + '   '.join(column_index) + '\n'

    # for row in range(self._rows):
    #   img += f'{self._alpha_list[row]} |'
    #   for col in range(self._cols):
    #     img += f' {self._grid[row][col]} |'
    #   img += '\n'
    self._renderer.draw()

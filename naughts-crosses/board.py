from grid import Grid

PLAYER_1 = 1
PLAYER_2 = 2

class Board:
  def __init__(self):
    self._grid = Grid()

    self._grid.add_player(PLAYER_1, 'A0')
    self._grid.add_player(PLAYER_2, 'A1')
    self._grid.add_player(PLAYER_1, 'C2')
    self._grid.add_player(PLAYER_2, 'A2')
    print(self._grid.add_player(PLAYER_1, 'B1'))
    self._grid.draw_grid()

from grid import Grid, Player
from text_gui import TextGUI

class Board:
  def __init__(self):
    self._grid = Grid(3, 3)
    self._text_gui = TextGUI(self._grid)
    self._current_player = Player.ONE


  def run(self) -> None:
    # Draw grid on startup
    self._text_gui.clear_console()
    self._text_gui.draw()

    is_running = True
    while(is_running):
      # If move is None quit
      move = self._text_gui.get_move(self._current_player)
      if move:
        player_wins = self._grid.add_player(self._current_player, move)

        # Draw the grid after adding the player
        self._text_gui.clear_console()
        self._text_gui.draw()

        if player_wins:
          play_again = self._text_gui.print_player_wins(self._current_player)
          if play_again:
            self._grid.clear_grid()
            self._text_gui.clear_console()
            self._text_gui.draw()
          else:
            is_running = False

        self._current_player = Player.ONE if self._current_player == Player.TWO else Player.TWO

      else:
        is_running = False

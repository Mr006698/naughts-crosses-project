from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

from grid import Grid

class KivyGUI(GridLayout):
  def __init__(self, grid: Grid, callback, **kwargs):
    super(KivyGUI, self).__init__(**kwargs)

    # Set grid layouts rows and columns
    self._grid = grid
    self.rows = grid._rows
    self.cols = grid._cols

    self._create_buttons(callback)


  def _create_buttons(self, callback) -> None:
    for row in range(self.rows):
      for col in range(self.cols):
        btn = Button(text=f'{row}, {col}', color=(1, 1, 1, 1), background_normal='static/images/square_cell.png')
        btn.fbind('on_press', callback, (row, col))
        self.add_widget(btn)

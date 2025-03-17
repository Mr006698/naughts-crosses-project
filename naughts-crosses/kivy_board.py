from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

from grid import Grid, Player
from kivy_gui import KivyGUI

class KivyBoard(App):
  def build(self):
    # Game setup variables
    self._current_player = Player.ONE
    self._player_one_colour = '89CFFD'
    self._player_two_colour = 'F94892'
    self._alt_text_colour = 'FBDF07'
    self._def_text_colour = 'FFFFFF'

    # Window title
    self.title = 'Hippo And Shrimp'

    # Main contents container
    box_layout = BoxLayout(orientation='vertical', padding=[100, 0])

    # Game heading
    game_heading = Label(
      text=self._create_title(),
      font_size='70',
      font_name='Forte',
      size_hint=(1, 0.3),
      markup=True)
    
    box_layout.add_widget(game_heading)

    # Game grid and GUI
    self._grid = Grid(3, 3)
    self._kivy_gui = KivyGUI(self._grid, self._add_player)
    box_layout.add_widget(self._kivy_gui)

    # Player instructions
    self._game_console = Label(
      text=self._create_text('Make your move.'),
      font_name='InkFree',
      font_size='30',
      size_hint=(1, 0.4),
      markup=True)
    
    box_layout.add_widget(self._game_console)

    # Add to kivy app
    return box_layout
  

  # Callback from gui
  def _add_player(self, loc, btn) -> None:
    match self._current_player:
      case Player.ONE:
        btn.background_disabled_normal = 'static/images/square_hippo.png'
        btn.background_color = self._player_one_colour

      case Player.TWO:
        btn.background_disabled_normal = 'static/images/square_shrimp.png'
        btn.background_color = self._player_two_colour

    btn.disabled = True

    win_state = self._grid.add_player_at_loc(self._current_player, loc, 3)
    print(loc)
    print(win_state)

    # Switch players
    self._current_player = Player.TWO if self._current_player == Player.ONE else Player.ONE
    self._game_console.text = self._create_text('Make your move.')
  

  def _create_title(self) -> str:
    title_list = self.title.split()
    title_fmt = [
      f'[color={self._player_one_colour}]{title_list[0]}[/color]',
      f'[color={self._alt_text_colour}]{title_list[1]}[/color]',
      f'[color={self._player_two_colour}]{title_list[2]}[/color]']
    
    return ' '.join(title_fmt)
  

  def _create_text(self, text: str) -> str:
    colour = self._player_one_colour if self._current_player == Player.ONE else self._player_two_colour
    return f'[color={colour}]PLAYER {self._current_player.name}[/color] {text}'

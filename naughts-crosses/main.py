import os
os.environ['KCFG_GRAPHICS_FULLSCREEN'] = '0'
os.environ['KCFG_GRAPHICS_RESIZABLE'] = '0'
os.environ['KCFG_GRAPHICS_WIDTH'] = '500'
os.environ['KFCG_GRAPHICS_HEIGHT'] = '600'

from kivy.core.window import Window
from kivy_board import KivyBoard

if __name__ == '__main__':
  Window.clearcolor = 'black'
  KivyBoard().run()
  
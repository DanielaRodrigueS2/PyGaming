from scripts.Game import Game
from scripts.screens.MenuScreen import MenuScreen

game = Game()

game.change_current_screen(MenuScreen(game))

game.run()
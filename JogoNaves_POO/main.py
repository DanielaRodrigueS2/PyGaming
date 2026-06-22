from scripts.Game import Game
from scripts.MenuScreen import MenuScreen

game = Game()

game.change_current_screen(MenuScreen(game))

game.run()
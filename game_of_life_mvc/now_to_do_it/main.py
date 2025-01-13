from tkinter import Tk
from game_controller import GameController
from grid_model import GridModel
from gui_view import GameView

if __name__ == '__main__':
    root = Tk()
    game = GridModel(150, 150 )
    view = GameView(root, game)
    controller = GameController(game, view)
    root.mainloop()

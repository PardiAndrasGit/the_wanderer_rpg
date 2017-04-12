from tkinter import *

map_1 = [
        [0,1,0,0,0,1,0,0,0,0],
        [0,1,0,1,0,1,0,0,0,0],
        [0,1,1,1,0,1,0,0,0,0],
        [0,0,0,0,0,1,0,0,0,0],
        [1,1,1,1,0,1,0,0,0,0],
        [0,1,0,0,0,1,0,0,0,0],
        [0,1,1,1,0,1,1,0,0,0],
        [0,0,0,0,0,1,1,0,0,0],
        [0,0,0,0,0,0,0,0,1,0],
        [0,0,0,0,0,0,1,0,1,1],
        ]

class GameLogic(object):
    def __init__(self, width = 0, height = 0):
        self.width = width
        self.height = height
        self.root = Tk()
        self.canvas = Canvas(self.root, width = self.width, height = self.height)
        self.canvas.pack()

        floormap = Map(self.canvas)

        self.root.mainloop()

class Map(object):
    def __init__(self, canvas):
        self.canvas = canvas
        self.map_display()

    def draw_floor_tile(self, x = 0, y = 0):
        self.canvas.create_image(x, y, anchor=NW, image=self.floor)

    def draw_wall_tile(self, x = 0, y = 0):
        self.canvas.create_image(x, y, anchor=NW, image=self.wall)

    def map_display(self):
        tile = 72
        self.wall = PhotoImage(file = "/Users/MrFox/OneDrive/greenfox/the_wanderer_rpg/img/wall.gif")
        self.floor = PhotoImage(file = "/Users/MrFox/OneDrive/greenfox/the_wanderer_rpg/img/floor.gif")
        for row in range(len(map_1)):
            for cell in range(len(map_1[row])):
                if map_1[cell][row] == 0:
                    self.draw_floor_tile(row*tile, cell*tile)
                else:
                    self.draw_wall_tile(row*tile, cell*tile)

class Character():
    pass

game = GameLogic("720", "720")

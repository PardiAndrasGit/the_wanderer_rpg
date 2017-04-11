from tkinter import *

map_1 = [
        [1,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        ]

class Map(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.root = Tk()
        self.canvas = Canvas(self.root, width = self.width, height = self.height)
        self.canvas.pack()

        self.display()
        self.root.mainloop()

    def draw_floor_tile(self, x = 0, y = 0):
        self.canvas.create_image(x, y, anchor="nw", image=self.floor)

    def draw_wall_tile(self, x = 0, y = 0):
        self.canvas.create_image(x, y, anchor="nw", image=self.wall)

    def display(self):
        self.floor = PhotoImage(file = "/Users/MrFox/OneDrive/greenfox/the_wanderer_rpg/img/floor.gif")
        self.wall = PhotoImage(file = "/Users/MrFox/OneDrive/greenfox/the_wanderer_rpg/img/wall.gif")
        for row in range(len(map_1)):
            for cell in range(len(map_1[row])):
                if map_1[cell][row] == 0:
                    self.draw_floor_tile(row*72, cell*72)
                else:
                    self.draw_wall_tile(row*72, cell*72)

floormap = Map("720", "720")

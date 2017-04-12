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
        # hero = Hero(self.canvas)
        hero = Character(self.canvas, "img/hero-down.gif")
        hero.draw_character(0, 0)

        self.root.mainloop()

class Map(object):
    def __init__(self, canvas):
        self.canvas = canvas
        self.floor = PhotoImage(file = "/Users/MrFox/OneDrive/greenfox/the_wanderer_rpg/img/floor.gif")
        self.wall = PhotoImage(file = "/Users/MrFox/OneDrive/greenfox/the_wanderer_rpg/img/wall.gif")

        self.map_display()

    def draw_floor_tile(self, x, y):
        self.canvas.create_image(x, y, anchor=NW, image=self.floor)

    def draw_wall_tile(self, x, y):
        self.canvas.create_image(x, y, anchor=NW, image=self.wall)

    def map_display(self):
        tile = 72
        for row in range(len(map_1)):
            for cell in range(len(map_1[row])):
                if map_1[cell][row] == 0:
                    self.draw_floor_tile(row*tile, cell*tile)
                else:
                    self.draw_wall_tile(row*tile, cell*tile)

class Character(object):
    def __init__(self, canvas, character_img):
        self.canvas = canvas
        self.character_img = character_img
        self.character_img = PhotoImage(file = character_img)

        # draw_character(0, 0)

    def draw_character(self, x, y):
        self.canvas.create_image(x, y, anchor=NW, image=self.character_img)

# class Hero(Character):
#     def __init__(self, canvas):
#         super().__init__(canvas)
#         self.character_img = PhotoImage(file = "/Users/MrFox/OneDrive/greenfox/the_wanderer_rpg/img/hero-down.gif")


game = GameLogic("720", "720")

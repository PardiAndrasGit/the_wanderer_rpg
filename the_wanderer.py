from tkinter import *
from boards import *


class GameLogic(object):
    def __init__(self, width = 0, height = 0):
        self.width = width
        self.height = height
        self.root = Tk()
        self.canvas = Canvas(self.root, width = self.width, height = self.height)

        self.canvas.pack()


        floormap = Map(self.canvas)
        hero = Hero(self.canvas)

        self.canvas.bind("<KeyPress>", hero.move_hero)

        self.canvas.focus_set()
        self.root.mainloop()

class Map(object):
    def __init__(self, canvas):
        self.canvas = canvas
        self.floor = PhotoImage(file = "/Users/MrFox/OneDrive/greenfox/the_wanderer_rpg/img/floor.gif")
        self.wall = PhotoImage(file = "/Users/MrFox/OneDrive/greenfox/the_wanderer_rpg/img/wall.gif")

        self.map_display(map_1)

    def draw_floor_tile(self, x, y):
        self.canvas.create_image(x, y, anchor=NW, image=self.floor)

    def draw_wall_tile(self, x, y):
        self.canvas.create_image(x, y, anchor=NW, image=self.wall)

    def map_display(self, board):
        tile = 72
        for row in range(len(board)):
            for cell in range(len(board[row])):
                if board[cell][row] == 0:
                    self.draw_floor_tile(row*tile, cell*tile)
                else:
                    self.draw_wall_tile(row*tile, cell*tile)

class Character(object):
    def __init__(self, canvas):
        self.canvas = canvas
        self.x = 0
        self.y = 0
        self.tile = 72

    def draw_character(self, x, y, character_img):
        self.canvas.create_image(x*self.tile, y*self.tile, anchor=NW, image=character_img)

class Hero(Character):
    def __init__(self, canvas):
        super().__init__(canvas)
        self.character_img_down = PhotoImage(file = "/Users/MrFox/OneDrive/greenfox/the_wanderer_rpg/img/hero-down.gif")
        self.character_img_up = PhotoImage(file = "/Users/MrFox/OneDrive/greenfox/the_wanderer_rpg/img/hero-up.gif")
        self.character_img_right = PhotoImage(file = "/Users/MrFox/OneDrive/greenfox/the_wanderer_rpg/img/hero-right.gif")
        self.character_img_left = PhotoImage(file = "/Users/MrFox/OneDrive/greenfox/the_wanderer_rpg/img/hero-left.gif")

        self.draw_character(self.x, self.y, self.character_img_down)

    def move_hero(self, e):
        if e.keycode == 8320768: # up
            if self.y > 0:
                self.y -= 1
                self.draw_character(self.x, self.y, self.character_img_up)
        elif e.keycode == 8255233: # down
            if self.y < 9:
                self.y += 1
                self.draw_character(self.x, self.y, self.character_img_down)
        elif e.keycode == 8189699: # right
            if self.x < 9:
                self.x += 1
                self.draw_character(self.x, self.y, self.character_img_right)
        elif e.keycode == 8124162: # left
            if self.x > 0:
                self.x -= 1
                self.draw_character(self.x, self.y, self.character_img_left)
                

        # box.draw(canvas)

game = GameLogic("720", "720")

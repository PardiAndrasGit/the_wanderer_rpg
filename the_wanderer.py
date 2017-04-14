from tkinter import *
from boards import *

class GameLogic(object):
    def __init__(self, width = 0, height = 0):
        self.width = width
        self.height = height
        self.root = Tk()
        self.canvas = Canvas(self.root, width = self.width, height = self.height)
        self.canvas.pack()

        self.floormap = Map(self.canvas)
        self.hero = Hero(self.canvas)

        self.canvas.bind("<KeyPress>", self.key_press)

        self.canvas.focus_set()
        self.root.mainloop()

    def key_press(self, e):
        if e.keycode == 8320768: # up
            self.hero.draw_character(self.hero.x, self.hero.y - 1, self.hero.character_img_up)
        elif e.keycode == 8255233: # down
            self.hero.draw_character(self.hero.x, self.hero.y + 1, self.hero.character_img_down)
        elif e.keycode == 8189699: # right
            self.hero.draw_character(self.hero.x + 1, self.hero.y, self.hero.character_img_right)
        elif e.keycode == 8124162: # left
            self.hero.draw_character(self.hero.x - 1, self.hero.y, self.hero.character_img_left)

class Map(object):
    def __init__(self, canvas):
        self.canvas = canvas
        self.floor = PhotoImage(file = "/Users/MrFox/OneDrive/greenfox/the_wanderer_rpg/img/floor.gif")
        self.wall = PhotoImage(file = "/Users/MrFox/OneDrive/greenfox/the_wanderer_rpg/img/wall.gif")
        self.level_map = map_1
        self.map_display(self.level_map)


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
        self.character_delete = 0

    def draw_character(self, x, y, character_img):
        self.canvas.delete(self.character_delete)
        self.character_delete = self.canvas.create_image(x*self.tile, y*self.tile, anchor=NW, image=character_img)

class Hero(Character):
    def __init__(self, canvas):
        super().__init__(canvas)
        self.character_img_down = PhotoImage(file = "/Users/MrFox/OneDrive/greenfox/the_wanderer_rpg/img/hero-down.gif")
        self.character_img_up = PhotoImage(file = "/Users/MrFox/OneDrive/greenfox/the_wanderer_rpg/img/hero-up.gif")
        self.character_img_right = PhotoImage(file = "/Users/MrFox/OneDrive/greenfox/the_wanderer_rpg/img/hero-right.gif")
        self.character_img_left = PhotoImage(file = "/Users/MrFox/OneDrive/greenfox/the_wanderer_rpg/img/hero-left.gif")

        self.draw_character(self.x, self.y, self.character_img_down)

    def draw_character(self, x, y, character_img):
        floormap = Map(self.canvas)
        if 0 <= x <= 9 and 0 <= y <= 9:
            if floormap.level_map[y][x] == 0:
                self.x = x
                self.y = y
                self.canvas.delete(self.character_delete)
                self.character_delete = self.canvas.create_image(x*self.tile, y*self.tile, anchor=NW, image=character_img)

game = GameLogic("720", "720")

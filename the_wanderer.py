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

    # def can_move(self):
    #     if floormap.get_tile_status() == True:
    #         hero.move_hero()

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

    def get_tile_status(self, board, x, y):
        if board[y][x] == 0:
            return True
        else:
            return False

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

    def move_hero(self, e):
        hero_on_map = Map(self.canvas)
        if e.keycode == 8320768: # up
            if self.y > 0:
                self.y -= 1
                if hero_on_map.get_tile_status(map_1, self.x, self.y) == True:
                    self.draw_character(self.x, self.y, self.character_img_up)
                else:
                    self.y += 1
                    self.draw_character(self.x, self.y, self.character_img_up)
        elif e.keycode == 8255233: # down
            if self.y < 9:
                self.y += 1
                if hero_on_map.get_tile_status(map_1, self.x, self.y) == True:
                    self.draw_character(self.x, self.y, self.character_img_down)
                else:
                    self.y -= 1
                    self.draw_character(self.x, self.y, self.character_img_down)
        elif e.keycode == 8189699: # right
            if self.x < 9:
                self.x += 1
                if hero_on_map.get_tile_status(map_1, self.x, self.y) == True:
                    self.draw_character(self.x, self.y, self.character_img_right)
                else:
                    self.x -= 1
                    self.draw_character(self.x, self.y, self.character_img_right)
        elif e.keycode == 8124162: # left
            if self.x > 0:
                self.x -= 1
                if hero_on_map.get_tile_status(map_1, self.x, self.y) == True:
                    self.draw_character(self.x, self.y, self.character_img_left)
                else:
                    self.x += 1
                    self.draw_character(self.x, self.y, self.character_img_left)

game = GameLogic("720", "720")

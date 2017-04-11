from tkinter import *

root = Tk()

canvas = Canvas(root, width='720', height='720', background="black")
canvas.pack()

class FloorTile(object):
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
        self.background = PhotoImage(file = "/Users/MrFox/OneDrive/greenfox/the_wanderer_rpg/img/floor.gif")
        self.walk_on = True

    def draw_floor_tile(self):
        for column in range(10):
            canvas.create_image(self.x, self.y, anchor="nw", image=self.background)
            self.y += 72

floormap = FloorTile()
floormap.draw_floor_tile()

root.mainloop()

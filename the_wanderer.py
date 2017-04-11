from tkinter import *

root = Tk()

canvas = Canvas(root, width='600', height='600')
canvas.pack()

class FloorTile(object):
    def __init__(self, x = 0, y = 0, size = 60):
        self.x = x
        self.y = y
        self.size = size
        # self.background = PhotoImage(file = "/Users/MrFox/OneDrive/greenfox/the_wanderer_rpg/img/floor.png")
        self.walk_on = True

    def draw_floor_tile(self):
        floor = canvas.create_rectangle(self.x,self.y, self.x+self.size,self.y+self.size)


floormap = FloorTile()
floormap.draw_floor_tile()

root.mainloop()

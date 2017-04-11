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
        canvas.create_image(0, 0, anchor="nw", image=self.background)


# self.horizon = PhotoImage(file = './assets/floor.png')
# 		self.canvas.create_image(0, self.height//4 * 3, anchor="nw", image=self.horizon)

floormap = FloorTile()
floormap.draw_floor_tile()

root.mainloop()

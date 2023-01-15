
import tkinter as tk
from tkinter import *

size = [1920, 1080]
size_scaled = [x*0.7 for x in size]
size_scaled_string = "x".join([str(int(x)) for x in size_scaled])
current_colour = "red"

main_window = tk.Tk()
main_window.geometry(size_scaled_string)

class DrawingCanvas():
    def __init__(self, root, bg_colour, size, grid_coords):
        self.canvas = Canvas(root, bg=bg_colour, width=size[0], height=size[1]) #create canvas
        self.canvas.grid(row=grid_coords[0], column=grid_coords[1]) #put canvas on screen

        self.canvas.bind("<Button-1>", self.get_coords)
        self.canvas.bind("<B1-Motion>", self.get_coords)

    def draw(self, **properties):
        #self.shape = properties["shape"]
        self.coords = properties["coords"]
        self.colour = properties["colour"]
        self.canvas.create_oval(*self.coords, *self.coords, fill=self.colour)

    def get_coords(self, event):
        self.draw(coords=(event.x, event.y), colour="white")

class Pen():
    pass

'''
move getting coords and events stuff to pen class
'''

canvas = DrawingCanvas(main_window, "brown", (size_scaled[0] * 0.7, size_scaled[1] * 0.7), (0, 0))

main_window.mainloop()
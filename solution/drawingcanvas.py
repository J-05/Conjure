import tkinter as tk
from tkinter import *

class DrawingCanvas(tk.Frame):
    def __init__(self, root, bg_colour, size, grid_coords, pen):
        tk.Frame.__init__(self, root)
        self.root = root
        self.bg_colour = bg_colour
        self.size = size
        self.grid_coords = grid_coords
        self.pen = pen
        self.canvas = Canvas(self.root, bg=self.get_bg_colour(), width=self.get_size()[0], height=self.get_size()[1]) #create canvas
        
        self.init_canvas()

    def init_canvas(self):
        self.canvas.grid(row=self.get_grid_coords()[0], column=self.get_grid_coords()[1]) #put canvas on screen
        self.canvas.bind("<Button-1>", self.touch_down)
        self.canvas.bind("<B1-Motion>", self.touch_down_move)

    def set_bg_colour(self, bg_colour):
        self.bg_colour = bg_colour

    def get_bg_colour(self):
        return self.bg_colour

    def set_size(self, size):
        self.size = size

    def get_size(self):
        return self.size

    def set_grid_coords(self, grid_coords):
        self.grid_coords = grid_coords

    def get_grid_coords(self):
        return self.grid_coords

    def create_circle(self, start_coords, end_coords, **kwargs):#---------------------------------------------------
        self.canvas.create_oval(*start_coords, *end_coords, fill= kwargs.get("fill", "White"), outline=kwargs.get("outline", "White"))

    def touch_down(self, event):
        self.create_circle(self.pen.get_coords(event), self.pen.get_coords(event), outline="white", fill="white")

    def touch_down_move(self, event):
        self.create_circle(self.pen.get_coords(event), self.pen.get_coords(event), fill="white", outline="white")
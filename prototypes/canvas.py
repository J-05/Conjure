import tkinter as tk
from tkinter import *
from tkinter import Canvas, colorchooser, Button, Label

class DrawingCanvas():
    def __init__(self, root, bg_colour, size, grid_coords()):
        self.canvas = Canvas(root, bg=bg_colour, width=size[0], height=size[1])
        self.canvas.grid(row=grid_coords[0], column=grid_coords[1])

    def draw(self, **properties):
        self.shape = properties["shape"]
        self.coords = properties["coords"]
        self.colour = properties["colour"]
        self.canvas.create_oval(*self.coords, *self.coords, fill=colour)

class Pen():
    def __init__(self):
        self.width = 0
        
    def pen_down(self):
        pass

    def pen_up(self):
        pass


#variables
size = [1920, 1080]
size_scaled = [x*0.7 for x in size]
size_scaled_string = "x".join([str(int(x)) for x in size_scaled])
current_colour = "red"

main_window = tk.Tk()
main_window.geometry(size_scaled_string)

def colour():
    global current_colour
    colour = colorchooser.askcolor()
    current_colour = colour[1]

def get_coords(event):
    global prev_x, prev_y
    prev_x, prev_y = event.x, event.y

def draw_line(event):
    global prev_x, prev_y, current_colour
    canvas.create_line((prev_x, prev_y, event.x, event.y), fill=current_colour, width=10)
    prev_x, prev_y = event.x, event.y

canvas = Canvas(main_window, bg="black", width=size_scaled[0] * 0.7, height=size_scaled[1] * 0.7)
canvas.pack(anchor="center", expand=1)

canvas.bind("<Button-1>", get_coords)
canvas.bind("<B1-Motion>", draw_line)

pick_colour_btn = Button(main_window, text="pick a colour", command=colour, anchor="s", height=5, width=10, fg="red", bg="grey").pack()

main_window.mainloop()
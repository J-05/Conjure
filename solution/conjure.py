import tkinter as tk
from tkinter import *
from drawingcanvas import DrawingCanvas
from pen import Pen

size = [1920, 1080]
size_scaled = [x*0.7 for x in size]
size_scaled_string = "x".join([str(int(x)) for x in size_scaled])
current_colour = "red"

main_window = tk.Tk()
main_window.geometry(size_scaled_string)

canvas = DrawingCanvas(main_window, "brown", (size_scaled[0] * 0.7, size_scaled[1] * 0.7), (0, 0), Pen())

main_window.mainloop()
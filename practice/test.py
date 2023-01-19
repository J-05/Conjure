import tkinter as tk
from tkinter import *

root = tk.Tk()
button = Button(root, text="hi")
button.pack()

def coords(event):
    print("hi")

button.bind("<Button-1>", coords)

root.mainloop()
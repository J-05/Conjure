import tkinter as tk
from tkinter import *
from tkinter import Canvas

#variables
size = [1920, 1080] #original size
size_scaled = [x*0.7 for x in size] #scaled down
size_scaled_string = "x".join([str(int(x)) for x in size_scaled]) #converted to numxnum

root = tk.Tk() #create window
root.geometry(size_scaled_string) #change size of window

##### WINDOW FRAME #####
window_frame = tk.Frame(root, bg="brown")
window_frame.grid(row=0, column=0, sticky=N+E+S+W)

##### MENU BAR - Contain the menu selections #####
menu_bar_frame = tk.Frame(window_frame, bg="red") #creates a frame that will house the menu buttons
menu_bar_frame.grid(row=0, column=0, columnspan=3, sticky=N+E+S+W) #puts the menu bar onto the main grid on root
#sticky NSEW ensures it spans the whole of the cell
#padx and pady move the menu bar away from the borders of the grid

##### LEFT PANEL - Contains the tool windows on the left #####
left_panel = tk.Frame(window_frame, bg="yellow", padx=10, pady=10, width=200)
left_panel.grid(row=1, column=0, sticky=W+N+S)

##### RIGHT PANEL - Contains the tool windows on the left #####
right_panel = tk.Frame(window_frame, bg="yellow", padx=10, pady=10, width=200) #pad doesnt work?------------------------------------
right_panel.grid(row=1, column=2, sticky=E+N+S)

##### TOP TOOLBAR - Contains the quick access tools on the top #####
top_toolbar = tk.Frame(window_frame, bg="blue", width=1000, height=50)
top_toolbar.grid(row=1, column=1, sticky=N)

##### BOTTOM TOOLBAR - Contains the quick access tools on the top #####
bottom_toolbar = tk.Frame(window_frame, bg="blue", width=1000, height=50)
bottom_toolbar.grid(row=1, column=1, sticky=S)

##### CANVAS #####
canvas = Canvas(window_frame, bg="white", width=size_scaled[0] * 0.7, height=size_scaled[1] * 0.7)
canvas.grid(row=1, column=1)


root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

window_frame.columnconfigure(0, weight=0) #the first column of root will have a weight of 1 (relative scaling)
window_frame.columnconfigure(1, weight=1) 
window_frame.columnconfigure(2, weight=0) 
window_frame.rowconfigure(0, weight=2)
window_frame.rowconfigure(1, weight=100)

root.mainloop()
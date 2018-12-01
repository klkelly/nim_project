#! usr/bin/env python3

from tkinter import *

class Nim(Frame):
    def __init__(self, master=None):
        super().__init__(master) # calls the constructor for the parent class
        self.master = master
        #grid = place in the grid, make it stretch to the user's setting
        self.grid(sticky=N+S+E+W)
        self.start()
    def start(self):
        pass

if __name__ = "__main__":
    root = Tk()
    app = Nim(master=root)
    app.mainloop()
from tkinter import *
from nim_text import *
import sys
#install tkinter before running this script

#application window
class Nim(Frame):
    def __init__(self, master=None):
        super().__init__(master) # calls the constructor for the parent class
        self.master = master
        #grid = place in the grid, make it stretch to the user's setting
        self.grid(sticky=N+S+E+W)
        #runs the create widget method
        self.create_widgets()

    def create_widgets(self):
        # makes it so that everything is centered
        top=self.winfo_toplevel()
        top.rowconfigure(0, weight=1)
        top.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        # creates a button with specific options
        self.hi_there = Button(self, cursor = "hand2")
        self.hi_there["text"] = "Existence is Pain\n(click me)"
        self.hi_there["command"] = self.say_hi
        # places in grid
        self.hi_there.grid(sticky=N+S+E+W)
        #game starter button
        self.start = Button(self, text = "wanna play a game?", command = self.play)
        self.start.grid(sticky=N+S+E+W)
        #quit button
        self.quit = Button(self, text="QUIT", fg="red",
                              command=self.stop)
        self.quit.grid(sticky=S+E+W)

        #creates another frame inside the bigger application frame
        # when clicked, it calls the clicked method. This is not a button
        self.box = Frame(self,width=100, height=100,cursor = "hand1")
        self.box.grid_propagate(0)
        self.boxception= Frame(self.box, width= 5, height = 5, bg="red")
        self.box.bind("<Button-1>", self.clicked)
        self.box.grid(sticky=N+S+E+W)
        self.boxception.grid(sticky=N+S+E+W)

    
    def recreate_widgets(self):
        self.back.destroy() 
         # creates a button with specific options
        self.hi_there = Button(self, cursor = "hand2")
        self.hi_there["text"] = "Existence is Pain\n(click me)"
        self.hi_there["command"] = self.say_hi
        # places in grid
        self.hi_there.grid(sticky=N+S+E+W)
        self.box = Frame(self,width=100, height=100,cursor = "hand1")
        self.box.grid_propagate(0)
        self.box.bind("<Button-1>", self.clicked)
        self.box.grid(sticky=N+S+E+W)
        self.box.grid_propagate()

    def clicked(self, event):
        print ("clicked at", event.x, event.y)
        if (self.box["bg"]=="yellow"):
            self.box.config(bg= "white")
        else:
            self.box.config(bg= "yellow")

    def say_hi(self):
        print("keven JUST PUSH")

    def play(self):
        print ("play")
        try:
            self.box.grid_remove()
            self.hi_there.destroy()
            self.start.destroy()
            self.back = Button(self, text = "Go Back", command = self.recreate_widgets)
            self.back.grid(sticky=N+S+E+W)
            self.game = Game()
            self.game.main()
        except RuntimeError:
            print ("bitch, just click once")

    # quits the whole program and destrys window, python stops running
    def stop(self):
        self.master.destroy()
        raise SystemExit

root = Tk()
app = Nim(master=root)
app.mainloop()

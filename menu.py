from tkinter import *
import time
from nim_text import *
import sys
#install tkinter before running this script

#application window
class StartMenu(Frame):
    def __init__(self, master=None):
        #idk what this does
        super().__init__(master)
        self.master = master
        #pack = place in the window
        self.pack()
        #runs the create widget method
        self.create_widgets()

    def create_widgets(self):
        # creates a button with specific options
        self.hi_there = Button(self, cursor = "hand2")
        self.hi_there["text"] = "Existence is Pain\n(click me)"
        self.hi_there["command"] = self.say_hi
        # packs that button
        self.hi_there.pack(side="top")
        #game starter button
        self.start = Button(self, text = "wanna play a game?", command = self.play)
        self.start.pack(side="right")
        #quit button
        self.quit = Button(self, text="QUIT", fg="red",
                              command=self.stop)
        self.quit.pack(side="bottom")

        #creates another frame inside the bigger application frame
        # when clicked, it calls the clicked method. This is not a button
        self.box = Frame(self,width=100, height=100,cursor = "hand1")
        self.box.bind("<Button-1>", self.clicked)
        self.box.pack(side="left")

    def clicked(self, event):
        print ("clicked at", event.x, event.y)
        if (self.box["bg"]=="yellow"):
            self.box.config(bg= "white")
        else:
            self.box.config(bg= "yellow")

    def say_hi(self):
        print("keven JUST PUSH")

    def play(self):
        try:
            self.game = Game()
            self.game.main()
        except RuntimeError:
            print ("bitch, just click once")
    # quits the whole program and destrys window, python stops running

    def stop(self):
        self.master.destroy()
        raise SystemExit

root = Tk()
app = StartMenu(master=root)
app.mainloop()
app.destroy()
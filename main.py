#! usr/bin/env python3

from tkinter import *

class Nim(Frame):
    def callconstructor(self, ref):
        super().__init__(ref)
    def __init__(self, master=None):
        self.callconstructor(master) # calls the constructor for the parent class
        self.master = master
        self.grid(sticky=N+S+E+W)
        self.mode = 0
        self.mode_labels = ["1vCPU", "1v1"]
        self.game = game(self)
        self.start()

    def start(self):
        self.game.grid_remove()
        self.start = start(self)
        self.start.grid(sticky=N+S+E+W)


    def rules(self):
        print("rules")
        pass

    def stack_set(self, var):
        self.stacks_mode = var
        self.stacks_modeLabel = Label(self, text=self.stacks_labels[self.stacks_mode])
        print (var)

    def play(self):
        print("play")
        self.start.grid_remove()
        self.game.grid(sticky=N+S+E+W)


    def quit(self):
        print("quitting")
        self.master.destroy()
        raise SystemExit

class start(Nim):
    def __init__(self, master=None): 
        super().callconstructor(master) # We call the frame constructor
        self.master = master # master is gonna be the instance of nim
        self.width = 3500
        self.height = 2000
        self.make_widgets()
    def make_widgets(self):
        # A window set up with a title, and buttons that will change options, plus a 'start game' option.
        # Title will be Nim; buttons will be pretty self-evident.
        self.vCPUbutton = Button(self, cursor = "hand2", text="1vCPU", command = self.mode_CPU)
        self.vPbutton = Button(self, cursor = "hand2", text="1v1", command = self.mode_PVP)
        self.playersLabel = Label(self, text = "Players:")
        self.welcomeLabel = Label(self, text = "Welcome to Nim!")
        self.rulesButton = Button(self, cursor = "hand2", text="Rules", command = self.master.rules)
        self.startButton = Button(self, cursor = "hand2", text="Start Game", command = self.master.play , fg="green")
        self.quitButton = Button(self, cursor = "hand2", text="Quit", command=self.quit,fg="red")
        self.player_modeLabel = Label(self, text=self.master.mode_labels[self.master.mode])
        self.welcomeLabel.grid(column=0, row=0, columnspan=2)
        self.playersLabel.grid(column=0, row=1)
        self.vCPUbutton.grid(column=0, row=2)
        self.vPbutton.grid(column=0, row=3)
        self.rulesButton.grid(column=0, row=5)
        self.startButton.grid(column=4, row=5)
        self.quitButton.grid(column=4, row=6)
        self.player_modeLabel.grid(column=4, row=2)

    def mode_CPU(self):
        self.master.mode = 0
        self.player_modeLabel["text"] = self.master.mode_labels[self.master.mode]
        #self.player_modeLabel.grid(column=4, row=2)        

    def mode_PVP(self):
        self.master.mode = 1
        self.player_modeLabel["text"] = self.master.mode_labels[self.master.mode]
        #self.player_modeLabel.grid(column=4, row=2)


    def quit(self):
        super().quit()

class game(Nim):
    def __init__(self,master=None):
        super().callconstructor(master) # We call the frame constructor
        self.master = master # master is gonna be the instance of nim
        self.width = 3500
        self.height = 2000
        self.make_widgets()
    def make_widgets(self):
        self.menuButton = Button(self, cursor = "hand2", text="Back to menu", command=self.master.start, fg="green")
        self.quitButton = Button(self, cursor = "hand2", text="Quit", command=self.quit,fg="red")
        self.menuButton.grid()
        self.quitButton.grid()
    def quit(self):
        super().quit()


if __name__ == "__main__":
    root = Tk()
    app = Nim(master=root)
    app.mainloop() 
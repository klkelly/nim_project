#! usr/bin/env python3

from tkinter import *

class Nim(Frame):
    def __init__(self, master=None):
        super().__init__(master) # calls the constructor for the parent class
        self.master = master
        #grid = place in the grid, make it stretch to the user's setting
        self.grid(sticky=N+S+E+W)
        self.start()
        self.mode = 0
        self.stacks_mode = 0
        self.stacks = []
    def start(self):
        
        self.mode_labels = ["1vCPU", "1v1"]
        self.stacks_labels = ["3", "4", "5", "6", "7"]
        # A window set up with a title, and buttons that will change options, plus a 'start game' option.
        # Title will be Nim; buttons will be pretty self-evident.
        self.vCPUbutton = Button(self, cursor = "hand2", text="1vCPU", command = self.mode_set(0))
        self.vPbutton = Button(self, cursor = "hand2", text="1v1", command = self.mode_set(1))
        self.playersLabel = Label(self, text = "Players:")
        self.welcomeLabel = Label(self, text = "Welcome to Nim!")
        self.stacksLabel = Label(self, text = "Stacks:")
        self.rulesButton = Button(self, cursor = "hand2", text="Rules", command = self.rules())
        self.startButton = Button(self, cursor = "hand2", text="Start Game", command=self.play(), fg="red")
        self.quitButton = Button(self, cursor = "hand2", text="Quit", command=self.quit())
        self.stacks3Button = Button(self, cursor = "hand2", text ="3", command = self.stack_set(0))
        self.stacks4Button = Button(self, cursor = "hand2", text ="4", command = self.stack_set(1))
        self.stacks5Button = Button(self, cursor = "hand2", text ="5", command = self.stack_set(2))
        self.stacks6Button = Button(self, cursor = "hand2", text ="6", command = self.stack_set(3))
        self.stacks7Button = Button(self, cursor = "hand2", text ="7", command = self.stack_set(4))
        self.player_modeLabel = Label(self, text=self.mode_labels[self.mode])
        self.stacks_modeLabel = Label(self, text=self.stacks_labels[self.stacks_mode])
        self.welcomeLabel.grid(column=0, row=0, columnspan=2)
        self.playersLabel.grid(column=0, row=1)
        self.stacksLabel.grid(column=1, row=1)
        self.vCPUbutton.grid(column=0, row=2)
        self.vPbutton.grid(column=0, row=3)
        self.rulesButton.grid(column=0, row=5)
        self.startButton.grid(column=4, row=5)
        self.quitButton.grid(column=4, row=6)
        self.stacks3Button.grid(column=1, row=2)
        self.stacks4Button.grid(column=1, row=3)
        self.stacks5Button.grid(column=1, row=4)
        self.stacks6Button.grid(column=1, row=5)
        self.stacks7Button.grid(column=1, row=6)
        self.player_modeLabel.grid(column=4, row=2)
        self.stacks_modeLabel.grid(column=4, row=3)

    def mode_set(self, var):
        self.mode = var
        self.player_modeLabel = Label(self, text=self.mode_labels[self.mode])

    def rules(self):
        pass

    def stack_set(self, var):
        self.stacks_mode = var
        self.stacks_modeLabel = Label(self, text=self.stacks_labels[self.stacks_mode])

    def play(self):
        pass

    def quit(self):
        pass

if __name__ == "__main__":
    root = Tk()
    app = Nim(master=root)
    app.mainloop() 
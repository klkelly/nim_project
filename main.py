#! usr/bin/env python3

from tkinter import *

class Nim(Frame):
    def callconstructor(self, ref):
        super().__init__(ref)
    def __init__(self, master=None):
        self.callconstructor(master) # calls the constructor for the parent class
        self.master = master
        self.grid(sticky=N+S+E+W)
        self.CPUplayer = 0
        self.misere = 0
        self.mode_labels = ["1vCPU", "1v1"]
        self.game = game(self)
        self.start = start(self)
        self.mainmenu()

    def mainmenu(self):
        self.game.grid_remove()
        self.start.grid(sticky=N+S+E+W)

    def classic_set(self):
        self.mode

    def mode_set(self, var):
        self.mode = var
        self.player_modeLabel = Label(self, text=self.mode_labels[self.mode])

    def rules(self):
        print("rules")

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
        # settings frame

        self.sett = LabelFrame(self,text="settings",labelanchor="n")

        self.sett.empty = Frame(self.sett,width=20) #spacer
        self.sett.vCPUbutton = Button(self.sett, cursor = "hand2", disabledforeground= "#999", text="1vCPU", command = self.mode_CPU)
        self.sett.vPbutton = Button(self.sett, cursor = "hand2", disabledforeground= "#999", text="1v1", command = self.mode_PVP)
        self.sett.mButton = Button(self.sett,cursor = "hand2", disabledforeground= "#999", text="misere", command = self.misere)
        self.sett.nButton = Button(self.sett,cursor = "hand2", disabledforeground= "#999", text="normal", command = self.normal)
        
        self.welcomeLabel = Label(self, text = "Welcome to Nim!")
        self.rulesButton = Button(self, cursor = "hand2", text="Rules", command = self.master.rules)
        self.startButton = Button(self, cursor = "hand2", text="Start Game", command = self.master.play , fg="green")
        self.quitButton = Button(self, cursor = "hand2", text="Quit", command=self.quit,fg="red")
        self.welcomeLabel.grid(column=0, row=0, columnspan=3,sticky=N+W+E+S)

        self.sett.grid(column=0,row=1,columnspan=3,sticky=N+W+E+S,ipadx=10,ipady=10,padx=10,pady=10)

        self.sett.vCPUbutton.grid(column=0, row=0,sticky=N+W+E+S)
        self.sett.vPbutton.grid(column=1, row=0,sticky=N+W+E+S)
        self.sett.empty.grid(column=2,row=0,sticky=N+W+E+S)
        self.sett.mButton.grid(column=3,row=0,sticky=N+W+E+S)
        self.sett.nButton.grid(column=4,row=0,sticky=N+W+E+S)

        self.rulesButton.grid(column=0, row=5,sticky=N+W+E+S)
        self.startButton.grid(column=1, row=5,sticky=N+W+E+S)
        self.quitButton.grid(column=2, row=5,sticky=N+W+E+S)


    def mode_CPU(self):
        self.master.CPUplayer = 1
        self.sett.vCPUbutton["state"]=DISABLED
        self.sett.vPbutton["state"]=NORMAL
        #self.player_modeLabel.grid(column=4, row=2)        

    def mode_PVP(self):
        self.master.CPUplayer = 0
        self.sett.vCPUbutton["state"]=NORMAL
        self.sett.vPbutton["state"]=DISABLED
        print("1v1")
        #self.player_modeLabel.grid(column=4, row=2)

    def misere(self):
        print("misere")
        self.master.misere= 1
        self.sett.mButton["state"]=DISABLED
        self.sett.nButton["state"]=NORMAL

    def normal(self):
        print("normal")
        self.master.misere=0
        self.sett.mButton["state"]=NORMAL
        self.sett.nButton["state"]=DISABLED

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
        self.menuButton = Button(self, cursor = "hand2", text="Back to menu", command=self.master.mainmenu, fg="green")
        self.quitButton = Button(self, cursor = "hand2", text="Quit", command=self.quit,fg="red")
        self.menuButton.grid()
        self.quitButton.grid()
    def quit(self):
        super().quit()


if __name__ == "__main__":
    root = Tk()
    app = Nim(master=root)
    app.mainloop() 
#! usr/bin/env python3

from tkinter import *
from random import randint

class Nim(Frame):
    def callconstructor(self, ref):
        super().__init__(ref)
    def __init__(self, master=None):
        self.callconstructor(master) # calls the constructor for the parent class
        self.master = master
        top= self.winfo_toplevel()
        top.title("Game of Nim By Keven and Rafa")
        self.grid(sticky=N+S+E+W)
        self.CPUplayer = 0
        self.misere = 0
        self.mode = "classic"
        self.stack=[3,4,5]
        self.game = game(self)
        self.start = start(self)
        self.diy = diy(self)
        self.instructions = instructions(self)
        self.mainmenu()

    def mainmenu(self):
        self.game.grid_remove()
        self.instructions.grid_remove()
        self.diy.grid_remove()
        self.start.grid(sticky=N+S+E+W)

    def rules(self):
        self.game.grid_remove()
        self.start.grid_remove()
        self.instructions.grid(sticky=N+S+E+W)

    def custom(self):
        self.game.grid_remove()
        self.start.grid_remove()
        self.instructions.grid_remove()
        self.diy.grid(sticky=N+S+E+W)

    def play(self):
        print("play")
        #makes the start menu dissapear, but it is not deleted
        self.start.grid_remove()
        self.diy.grid_remove()
        self.instructions.grid_remove()
        #makes the game appear
        #create a new game
        print(self.stack)
        self.game = game(self)
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

        self.sett = LabelFrame(self,text="Settings",labelanchor="n")

        self.sett.empty = Frame(self.sett,width=20) #spacer
        self.sett.vCPUbutton = Button(self.sett, cursor = "hand2", disabledforeground= "#999", text="1vCPU", command = lambda: self.mode_CPU(1))
        self.sett.vPbutton = Button(self.sett, cursor = "hand2", disabledforeground= "#999", text="1v1", command = lambda: self.mode_CPU(0))
        self.sett.mButton = Button(self.sett,cursor = "hand2", disabledforeground= "#999", text="misere", command = lambda: self.misere(1))
        self.sett.nButton = Button(self.sett,cursor = "hand2", disabledforeground= "#999", text="normal", command = lambda: self.misere(0))
        self.sett.clButton = Button(self.sett,cursor = "hand2", disabledforeground= "#999", text="classic", command = lambda: self.change_mode(0))
        self.sett.grButton = Button(self.sett,cursor = "hand2", disabledforeground= "#999", text="greedy", command = lambda: self.change_mode(1))
        self.sett.cuButton = Button(self.sett,cursor = "hand2", disabledforeground= "#999", text="custom", command =self.master.custom)
        self.welcomeLabel = Label(self, text = "Welcome to Nim!")
        self.rulesButton = Button(self, cursor = "hand2", text="Rules", command = self.master.rules)
        self.startButton = Button(self, cursor = "hand2", text="Start Game", command = self.master.play , fg="green")
        self.quitButton = Button(self, cursor = "hand2", text="Quit", command=self.quit,fg="red")
        self.welcomeLabel.grid(column=0, row=0, columnspan=3,sticky=N+W+E+S)

        self.sett.grid(column=0,row=1,columnspan=3,sticky=N+W+E+S,padx=10,pady=10)

        self.sett.vCPUbutton.grid(column=0, row=0,sticky=N+W+E+S)
        self.sett.vPbutton.grid(column=1, row=0,sticky=N+W+E+S)
        self.sett.empty.grid(column=2,row=0,sticky=N+W+E+S)
        self.sett.mButton.grid(column=3,row=0,sticky=N+W+E+S)
        self.sett.nButton.grid(column=4,row=0,sticky=N+W+E+S)
        self.sett.clButton.grid(column= 1, row=1,sticky=N+W+E+S)
        self.sett.grButton.grid(column= 2, row=1,sticky=N+W+E+S)
        self.sett.cuButton.grid(column= 3, row=1,sticky=N+W+E+S)

        self.rulesButton.grid(column=0, row=5,sticky=N+W+E+S)
        self.startButton.grid(column=1, row=5,sticky=N+W+E+S)
        self.quitButton.grid(column=2, row=5,sticky=N+W+E+S)


    def mode_CPU(self, var):
        # assign value to the attribute
        self.master.CPUplayer = var
        # if cpu player is activated
        if self.master.CPUplayer:
            #you cant click on the cpu button again
            self.sett.vCPUbutton["state"]=DISABLED
            self.sett.vPbutton["state"]=NORMAL
        else:
            self.sett.vCPUbutton["state"]=NORMAL
            self.sett.vPbutton["state"]=DISABLED


    def misere(self, var):
        self.master.misere = var
        if self.master.misere:
            self.sett.mButton["state"]=DISABLED
            self.sett.nButton["state"]=NORMAL
        else:
            self.sett.mButton["state"]=NORMAL
            self.sett.nButton["state"]=DISABLED

    def change_mode(self,var):
        if var == 0:
            self.master.mode = "classic"
            self.sett.clButton["state"]=DISABLED
            self.sett.grButton["state"]=NORMAL
            self.sett.cuButton["state"]=NORMAL
        elif var == 1:
            self.master.mode = "greedy"
            self.sett.grButton["state"]=DISABLED
            self.sett.clButton["state"]=NORMAL
            self.sett.cuButton["state"]=NORMAL
        elif var == 2:
            self.master.mode = "custom"
            self.sett.cuButton["state"]=DISABLED
            self.sett.grButton["state"]=NORMAL
            self.sett.clButton["state"]=NORMAL

    def quit(self):
        super().quit()


class game(Nim):
    def __init__(self,master=None):
        super().callconstructor(master) # We call the frame constructor
        self.master = master # master is gonna be the instance of nim
        self.turn = 1
        self.stack = self.master.stack
        self.gameOver = 0
        self.lastPlay = 0
        self.make_widgets()
        self.stack_selected= None

    def make_widgets(self):
        self.menuButton = Button(self, cursor = "hand2", text="Back to menu", command=self.master.mainmenu, fg="blue")
        self.quitButton = Button(self, cursor = "hand2", text="Quit", command=self.quit,fg="red")
        self.nextButton = Button(self, cursor = "hand2", text="Finish your turn", command=self.next_turn)
        self.turnLabel = Label(self, text = self.print_turn())
        self.container = LabelFrame(self, text = "Click to remove one from any stack",labelanchor ="n")
        self.container.grid(column = 0, row = 1, columnspan=3)
        self.stackbuttons=[]
        self.menuButton.grid(column = 0, row = 3)
        self.quitButton.grid(column = 2,row=3)
        self.nextButton.grid(column=1,row=2)
        self.turnLabel.grid(column=2, row= 0)

        for i in range(len(self.stack)):
            butt = Button(self.container,cursor = "hand2", disabledforeground= "#999",text = self.stack[i],command= lambda a=i: self.remove_one(a))
            self.stackbuttons.append(butt)
            self.stackbuttons[i].grid(column=i,row= 0,sticky = E+W)

    def remove_one(self,a):
        if self.stack_selected == a or self.stack_selected == None:
            self.stack_selected = a
            if self.stack[a]>0:
                self.stack[a] -= 1
                self.stackbuttons[a]["text"]=self.stack[a]
            if self.stack[a]==0:
                self.stackbuttons[a]["state"]=DISABLED
            self.check_win()
        else:
            print("you cant select two different stacks")
    
    def check_win(self):
        if all([ i==0 for i in self.stack]):
            if self.gameOver == 0:
                self.lastPlay = self.turn
                if not self.master.misere:
                    self.turnLabel["text"] = self.print_turn()
            self.gameOver = 1
            if not self.master.misere:
                self.turnLabel["text"] = self.print_turn()
            self.nextButton["state"]=DISABLED


    def next_turn(self):
        # do nothing if the player has not clicked on a stack yet
        if self.stack_selected == None:
            print("you must click on some stack before your turn ends")
            return
        self.turn = not self.turn
        self.turnLabel["text"]= self.print_turn()
        self.stack_selected = None
        if self.master.CPUplayer:
            self.cpu_turn()
            self.turn = not self.turn
            self.turnLabel["text"]= self.print_turn()
            self.stack_selected = None
        self.check_win()


# algorithm goes here
    def cpu_turn(self):
        nim_sum = 0
        for i in range(len(self.stack)):
            nim_sum = nim_sum^self.stack[i]
        if self.master.misere:
            stacks_left = 0
            big_stacks = 0
            for i in self.stack:
                if i > 0:
                    stacks_left += 1
                if i > 1:
                    big_stacks += 1
            if stacks_left % 2:
                if big_stacks == 1:
                    for i in range(len(self.stack)):
                        if self.stack[i] > 1:
                            self.stack[i] = 1
                            self.stackbuttons[i]["text"] = self.stack[i]
                            if self.stack[i] == 0:
                                self.stackbuttons[i]["state"]=DISABLED
                            break
                elif big_stacks > 1:
                    for i in range(len(self.stack)):
                        if self.stack[i]^nim_sum < self.stack[i]:
                            self.stack[i] = self.stack[i]^nim_sum
                            self.stackbuttons[i]["text"] = self.stack[i]
                            if self.stack[i] == 0:
                                self.stackbuttons[i]["state"]=DISABLED
                            break
                else:
                    ran1 = randint(0,len(self.stack)-1)
                    while not self.stack[ran1]:
                        ran1 = randint(0,len(self.stack)-1)
                    ran2 = randint(1,self.stack[ran1])
                    self.stack[ran1] -= ran2
                    self.stackbuttons[ran1]["text"] = self.stack[ran1]
                    if self.stack[ran1] == 0:
                        self.stackbuttons[ran1]["state"]=DISABLED
            else:
                if big_stacks == 1:
                    for i in range(len(self.stack)):
                        if self.stack[i] > 1:
                            self.stack[i] = 0
                            self.stackbuttons[i]["text"] = self.stack[i]
                            if self.stack[i] == 0:
                                self.stackbuttons[i]["state"]=DISABLED
                            break
                elif big_stacks == 0:
                    for i in range(len(self.stack)):
                        if self.stack[i] > 0:
                            self.stack[i] = 0
                            self.stackbuttons[i]["text"] = self.stack[i]
                            if self.stack[i] == 0:
                                self.stackbuttons[i]["state"]=DISABLED
                            break
                else:
                    if nim_sum == 0:
                        ran1 = randint(0,len(self.stack)-1)
                        while not self.stack[ran1]:
                            ran1 = randint(0,len(self.stack)-1)
                        ran2 = randint(1,self.stack[ran1])
                        self.stack[ran1] -= ran2
                        self.stackbuttons[ran1]["text"] = self.stack[ran1]
                        if self.stack[ran1] == 0:
                            self.stackbuttons[ran1]["state"]=DISABLED

                    else:
                        for i in range(len(self.stack)):
                            if self.stack[i]^nim_sum < self.stack[i]:
                                self.stack[i] = self.stack[i]^nim_sum
                                self.stackbuttons[i]["text"] = self.stack[i]
                                if self.stack[i] == 0:
                                    self.stackbuttons[i]["state"]=DISABLED
                                break

        else:
            if nim_sum == 0:
                ran1 = randint(0,len(self.stack)-1)
                while not self.stack[ran1]:
                    ran1 = randint(0,len(self.stack)-1)
                ran2 = randint(1,self.stack[ran1])
                self.stack[ran1] -= ran2
                self.stackbuttons[ran1]["text"] = self.stack[ran1]
                if self.stack[ran1] == 0:
                    self.stackbuttons[ran1]["state"]=DISABLED
            else:
                for i in range(len(self.stack)):
                    if self.stack[i]^nim_sum < self.stack[i]:
                        self.stack[i] = self.stack[i]^nim_sum
                        self.stackbuttons[i]["text"] = self.stack[i]
                        if self.stack[i] == 0:
                            self.stackbuttons[i]["state"]=DISABLED
                        break


        print("im a robot weeeee")

    def print_turn(self):
        if self.gameOver == 1:
            if self.master.misere:
                #player 1 had the last turn
                if self.lastPlay:
                    if self.master.CPUplayer == 0:
                        self.turnLabel["text"] = "Player 2 wins!"
                    else:
                        self.turnLabel["text"] = "CPU wins!"
                #player 2 had the last turn
                else:
                    self.turnLabel["text"] = "Player 1 wins!"
            # in normal version, the last to get an item wins
            else:
                #player 1 had the last turn
                if not self.lastPlay:
                    self.turnLabel["text"] = "Player 1 wins!"
                #player 2 had the last turn
                else:
                    if self.master.CPUplayer == 0:
                        self.turnLabel["text"] = "Player 2 wins!"
                    else:
                        self.turnLabel["text"] = "CPU wins!"
        else:
            if self.turn:
                return("Player 1's turn")
            else:
                return("Player 2's turn")

    def quit(self):
        super().quit()


class instructions(Nim):
    def __init__(self,master=None):
        super().callconstructor(master) # We call the frame constructor
        self.master = master
        self.make_widgets()
    def make_widgets(self):
        self.menuButton = Button(self, cursor = "hand2", text="Back to menu", command=self.master.mainmenu, fg="blue")
        self.quitButton = Button(self, cursor = "hand2", text="Quit", command=self.quit,fg="red")
        self.rulesText = Text(self, width=50, height=20, wrap="word")
        self.rulesText.insert('1.0', ('From Wikipedia: Nim is a mathematical game of strategy in which two players take '
            'turns removing objects from distinct heaps or piles. On each turn, a player must remove at least one object'
            ', and may remove any number of objects provided they all come from the same heap/pile. The goal of the game'
            ' is to be the player who removes the last object.\n\nIn our implementation of this game, players will take'
            ' turns removing objects from what we have called "stacks". There are two modes of play:\n  In Misere-mode, t'
            'he object of the game is to avoid taking the last object from the last remaining stack. Taking the last obj'
            'ect will result in the player losing the game!\n  In Normal-mode, the player who takes the last object from'
            'the last stack wins!'))
        self.menuButton.grid(column=0, row=1)
        self.quitButton.grid(column=0, row=2)
        self.rulesText.grid(column=0, row=0)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
    def quit(self):
        super().quit()


class diy(Nim):
    def __init__(self,master=None):
        super().callconstructor(master) # We call the frame constructor
        self.master = master
        self.stacknum= 0
        self.make_widgets()

    def make_widgets(self):
        self.menuButton = Button(self, cursor = "hand2", text="Back to menu", command=self.master.mainmenu, fg="blue")
        self.quitButton = Button(self, cursor = "hand2", text="Quit", command=self.quit,fg="red")
        self.startButton = Button(self, cursor = "hand2", text="Start Game", command = self.master.play , fg="green")
        # settings container
        self.sett = LabelFrame(self,text = "Customize your game",labelanchor ="n")
        self.sett.empty0 = Frame(self.sett,width=20) #spacer
        self.sett.empty1 = Frame(self.sett,width=20) #spacer
        self.stacknum = IntVar()
        self.sett.slider = Scale(self.sett, variable=self.stacknum,from_= 1, to= 9,length=200,orient=HORIZONTAL, label="Number of stacks",command = self.change_stack)
        self.sett.vCPUbutton = Button(self.sett, cursor = "hand2", disabledforeground= "#999", text="1vCPU", command = lambda: self.mode_CPU(1))
        self.sett.vPbutton = Button(self.sett, cursor = "hand2", disabledforeground= "#999", text="1v1", command = lambda: self.mode_CPU(0))
        self.sett.mButton = Button(self.sett,cursor = "hand2", disabledforeground= "#999", text="misere", command = lambda: self.misere(1))
        self.sett.nButton = Button(self.sett,cursor = "hand2", disabledforeground= "#999", text="normal", command = lambda: self.misere(0))
        self.sett.clButton = Button(self.sett,cursor = "hand2", disabledforeground= "#999", text="classic", command = lambda: self.change_mode(0))
        self.sett.grButton = Button(self.sett,cursor = "hand2", disabledforeground= "#999", text="greedy", command = lambda: self.change_mode(1))
        
        self.menuButton.grid(column=0, row=2)
        self.quitButton.grid(column=2, row=2)
        self.startButton.grid(column=1,row=2)

        self.sett.grid(column=0,row=1,columnspan=3,sticky=N+W+E+S,padx=10,pady=10)
        self.sett.slider.grid(column=0,row=0,columnspan=8)
        self.sett.vCPUbutton.grid(column=0,row=1)
        self.sett.vPbutton.grid(column=1,row=1)
        self.sett.empty0.grid(column=2,row=1)
        self.sett.mButton.grid(column=3,row=1)
        self.sett.nButton.grid(column=4,row=1)
        self.sett.empty1.grid(column=5,row=1)
        self.sett.clButton.grid(column=6,row=1)
        self.sett.grButton.grid(column=7,row=1)

    def change_stack(self,num):
        number= self.stacknum.get()
        self.master.stack =[]
        #randomly populates the stacks
        for i in range(number):
            x = randint(1,9)
            self.master.stack.append(x)

    def mode_CPU(self, var):
        # assign value to the attribute
        self.master.CPUplayer = var
        # if cpu player is activated
        if self.master.CPUplayer:
            #you cant click on the cpu button again
            self.sett.vCPUbutton["state"]=DISABLED
            self.sett.vPbutton["state"]=NORMAL
        else:
            self.sett.vCPUbutton["state"]=NORMAL
            self.sett.vPbutton["state"]=DISABLED


    def misere(self, var):
        self.master.misere = var
        if self.master.misere:
            self.sett.mButton["state"]=DISABLED
            self.sett.nButton["state"]=NORMAL
        else:
            self.sett.mButton["state"]=NORMAL
            self.sett.nButton["state"]=DISABLED

    def change_mode(self,var):
        if var == 0:
            self.master.mode = "classic"
            self.sett.clButton["state"]=DISABLED
            self.sett.grButton["state"]=NORMAL
        elif var == 1:
            self.master.mode = "greedy"
            self.sett.grButton["state"]=DISABLED
            self.sett.clButton["state"]=NORMAL

    def quit(self):
        super().quit()

if __name__ == "__main__":
    root = Tk()
    app = Nim(master=root)
    app.mainloop() 
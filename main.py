#! usr/bin/env python3

#
from tkinter import *
from random import randint

# widget that controls the whole game, child of a frame widget ()
class Nim(Frame):
    def callconstructor(self, ref):
        super().__init__(ref)
    def __init__(self, master=None):
        self.callconstructor(master) # calls the constructor for the parent class
        self.master = master
        top= self.winfo_toplevel()
        top.title("Game of Nim By Keven and Rafa")
        self.grid(sticky=N+S+E+W)
        # class attribute initialization
        self.CPUplayer = 0
        self.misere = 0
        self.mode = "classic"
        self.stacknum = 3
        # create children
        self.game = game(self)
        self.start = start(self)
        self.diy = diy(self)
        self.instructions = instructions(self)
        self.mainmenu()

    # displays main menu
    def mainmenu(self):
        # remove other children widgets from being shown on screen
        self.game.grid_remove()
        self.instructions.grid_remove()
        self.diy.grid_remove()
        # place the start widget on the screen
        self.start.grid(sticky=N+S+E+W)

    # displays rules
    def rules(self):
        # remove other children widgets from being shown on screen
        self.game.grid_remove()
        self.start.grid_remove()
        self.diy.grid_remove()
        # place the instructions widget on the screen
        self.instructions.grid(sticky=N+S+E+W)

    # displays the customize window
    def custom(self):
        # remove other children widgets from being shown on screen
        self.game.grid_remove()
        self.start.grid_remove()
        self.instructions.grid_remove()
        # place the diy widget on the screen
        self.diy.grid(sticky=N+S+E+W)

    # displays game window
    def play(self):
        #makes the other children disappear
        self.start.grid_remove()
        self.diy.grid_remove()
        self.instructions.grid_remove()
        #creates a new game with current settings
        self.game = game(self)
        self.game.grid(sticky=N+S+E+W)

    # destroys window then exits program
    def quit(self):
        print("quitting")
        self.master.destroy()
        raise SystemExit

# widget that contains what we see in the menu
class start(Nim):
    def __init__(self, master=None): 
        super().callconstructor(master) # We call the grandparent constructor
        self.master = master # master is gonna be the parent instance
        self.make_widgets()

    # creates all the visible widgets
    def make_widgets(self):
        # A window set up with a title, and buttons that will change options, plus a 'start game' option.
        # buttons will be pretty self-evident.
        # settings frame, parent of the buttons that go in it, child of the start widget
        self.sett = LabelFrame(self,text="Settings",labelanchor="n")
        # settings' children
        self.sett.empty = Frame(self.sett,width=20) #empty spacer for aesthetic purposes
        self.sett.vCPUbutton = Button(self.sett, cursor = "hand2", disabledforeground= "#999", text="1vCPU", command = lambda: self.mode_CPU(1))
        self.sett.vPbutton = Button(self.sett, cursor = "hand2", disabledforeground= "#999", text="1v1", command = lambda: self.mode_CPU(0))
        self.sett.mButton = Button(self.sett,cursor = "hand2", disabledforeground= "#999", text="misere", command = lambda: self.misere(1))
        self.sett.nButton = Button(self.sett,cursor = "hand2", disabledforeground= "#999", text="normal", command = lambda: self.misere(0))
        self.sett.clButton = Button(self.sett,cursor = "hand2", disabledforeground= "#999", text="classic", command = lambda: self.change_mode(0))
        self.sett.grButton = Button(self.sett,cursor = "hand2", disabledforeground= "#999", text="greedy", command = lambda: self.change_mode(1))
        self.sett.cuButton = Button(self.sett,cursor = "hand2", disabledforeground= "#999", text="custom", command =self.master.custom)
        # start's children widgets
        self.welcomeLabel = Label(self, text = "Welcome to Nim!")
        self.rulesButton = Button(self, cursor = "hand2", text="Rules", command = self.master.rules)
        self.startButton = Button(self, cursor = "hand2", text="Start Game", command = self.master.play , fg="green")
        self.quitButton = Button(self, cursor = "hand2", text="Quit", command=self.quit,fg="red")
        self.welcomeLabel.grid(column=0, row=0, columnspan=3,sticky=N+W+E+S)

        # grid method makes them appear on screen
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

    # callback functon that determines whether the game will be against another human or the computer
    # args: var, either 1 or 0 depending on whether game is against the computer or another player
    def mode_CPU(self, var):
        self.master.CPUplayer = var
        # if cpu player is activated
        if self.master.CPUplayer:
            # user can't click on the 1vCPU button again
            self.sett.vCPUbutton["state"]=DISABLED
            self.sett.vPbutton["state"]=NORMAL
        else:
            # user can't click on the 1v1 button again
            self.sett.vCPUbutton["state"]=NORMAL
            self.sett.vPbutton["state"]=DISABLED

    # callback function that determins whethe the game will be in misere mode or not
    # args: var, either 1 or 0
    def misere(self, var):
        self.master.misere = var
        # if misere version is activated
        if self.master.misere:
            # user can't click on the misere button again
            self.sett.mButton["state"]=DISABLED
            self.sett.nButton["state"]=NORMAL
        else:
            # user can't click on the normal button again
            self.sett.mButton["state"]=NORMAL
            self.sett.nButton["state"]=DISABLED
    #
    def change_mode(self,var):
        # set standard stack number to 3
        self.master.stacknum = 3
        if var == 0:
            # user can't click on classic button again
            self.master.mode = "classic"
            self.sett.clButton["state"]=DISABLED
            self.sett.grButton["state"]=NORMAL
            self.sett.cuButton["state"]=NORMAL
        elif var == 1:
            # user can't click on greedy button again
            self.master.mode = "greedy"
            self.sett.grButton["state"]=DISABLED
            self.sett.clButton["state"]=NORMAL
            self.sett.cuButton["state"]=NORMAL

    # calls parent's quit method
    def quit(self):
        super().quit()

# widget that controls what is shown during the gameplay, child of the Nim widget
class game(Nim):
    def __init__(self,master=None):
        super().callconstructor(master) # We call the frame constructor
        self.master = master # master is gonna be the instance of nim
        self.turn = 1
        self.gameOver = 0
        self.lastPlay = 0
        self.stack = []
        # randomizes stack contents
        for i in range(self.master.stacknum):
            x = randint(1,9)
            self.stack.append(x)
        self.stack_selected= None
        self.make_widgets()

    # creates all the visible widgets
    def make_widgets(self):
        #  game's children widgets
        self.menuButton = Button(self, cursor = "hand2", text = "Back to menu", command=self.master.mainmenu, fg = "blue")
        self.quitButton = Button(self, cursor = "hand2", text = "Quit", command = self.quit,fg = "red")
        self.nextButton = Button(self, cursor = "hand2", text = "Finish your turn", command = self.next_turn)
        self.turnLabel = Label(self, text = self.print_turn())
        self.gameLabel = Label(self, text = self.game_tag(),fg = "#999")
        self.container = LabelFrame(self, text = "Click to remove one from any stack",labelanchor = "n")
        self.stackbuttons=[]
        # places widgets on screen
        self.container.grid(column = 0, row = 1, columnspan=3)
        self.menuButton.grid(column = 0, row = 3)
        self.quitButton.grid(column = 2,row=3)
        self.nextButton.grid(column=1,row=2)
        self.gameLabel.grid(column = 0,row= 0)
        self.turnLabel.grid(column=2, row= 0)

        # creates stack buttons as children of self.container
        for i in range(len(self.stack)):
            butt = Button(self.container, cursor = "hand2", disabledforeground= "#999", text = self.stack[i], command = lambda a = i: self.remove_one(a))
            self.stackbuttons.append(butt)
            # places button on screen
            self.stackbuttons[i].grid(column = i,row = 0,sticky = E+W)

    # creates text that goes on the upper left corner
    # returns: text that describes what kind of game is being played
    def game_tag(self):
        tag = str(self.master.mode)
        if self.master.misere:
            tag +=" misere"
        else:
            tag +=" normal"
        if self.master.CPUplayer:
            tag += " vs CPU"
        else:
            tag += " vs Player 2"
        return (tag)

    # this is run everytime a stack button is clicked. It makes sure the click is valid,
    # if it is, it decreases the size of the stack by one.
    # args: a, index of the clicked stack
    def remove_one(self,a):
        # for greedy mode it checks if clicked stack is in fact the biggest one
        # if no stack is selected, it means it is a new turn
        if self.master.mode =="greedy" and self.stack_selected == None:
            # checks if stack clicked is smaller that any other stack
            if any([i > self.stack[a] for i in self.stack]):
                print ("you must select from the biggest pile(s)")
                # stops the function since the user is only allowed to click on the biggest
                return
        # checks if stack clicked is the same one as previous
        # if no stack is selected, it is a new turn. therefore any stack is valid
        # if a stack is already selected, the clicked stack has to be the same as what was clicked before
        if self.stack_selected == a or self.stack_selected == None:
            # selected stack becomes clicked stack until the method self.next_turn is called
            self.stack_selected = a
            if self.stack[a]>0:
                self.stack[a] -= 1
                # updates the appearance of stack button
                self.stackbuttons[a]["text"]=self.stack[a]
            # once the stack reaches size 0, the button that represents it is disabled
            # that way that button can't call this method if clicked again
            if self.stack[a]==0:
                self.stackbuttons[a]["state"]=DISABLED
            # check for a win condition after any change to the stack
            self.check_win()
        else:
            print("you can't select two different stacks")

    # checks if someone has won the game
    def check_win(self):
        # checks that all stacks are zero
        if all([ i==0 for i in self.stack]):
            # records current turn as last turn
            if self.gameOver == 0:
                self.lastPlay = self.turn
            self.gameOver = 1
            # updates text on the upper right corner to say who won
            self.turnLabel["text"] = self.print_turn()
            # prevents user from clicking on the next turn button again
            self.nextButton["state"] = DISABLED

    # changes turn, triggers CPU turn if enabled
    def next_turn(self):
        # do nothing if the player has not clicked on a stack yet
        if self.stack_selected == None:
            print("you must click on some stack before your turn ends")
            return
        self.turn = not self.turn
        self.turnLabel["text"]= self.print_turn()
        # make selected stack be none
        self.stack_selected = None
        # trigger CPU turn
        if self.master.CPUplayer:
            self.cpu_turn()
            self.check_win()
            # if no one has won yet, update turn lable again
            if self.gameOver == 0:
                self.turn = not self.turn
                self.turnLabel["text"]= self.print_turn()
                self.stack_selected = None


    # CPU if tree
    def cpu_turn(self):
        nim_sum = 0
        for i in range(len(self.stack)):
            nim_sum = nim_sum^self.stack[i]
        if self.master.mode != "greedy":
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
                                break
                    elif big_stacks > 1:
                        for i in range(len(self.stack)):
                            if self.stack[i]^nim_sum < self.stack[i]:
                                self.stack[i] = self.stack[i]^nim_sum
                                break
                    else:
                        ran1 = randint(0,len(self.stack)-1)
                        while not self.stack[ran1]:
                            ran1 = randint(0,len(self.stack)-1)
                        ran2 = randint(1,self.stack[ran1])
                        self.stack[ran1] -= ran2
                else:
                    if big_stacks == 1:
                        for i in range(len(self.stack)):
                            if self.stack[i] > 1:
                                self.stack[i] = 0
                                break
                    elif big_stacks == 0:
                        for i in range(len(self.stack)):
                            if self.stack[i] > 0:
                                self.stack[i] = 0
                                break
                    else:
                        if nim_sum == 0:
                            ran1 = randint(0,len(self.stack)-1)
                            while not self.stack[ran1]:
                                ran1 = randint(0,len(self.stack)-1)
                            ran2 = randint(1,self.stack[ran1])
                            self.stack[ran1] -= ran2

                        else:
                            for i in range(len(self.stack)):
                                if self.stack[i]^nim_sum < self.stack[i]:
                                    self.stack[i] = self.stack[i]^nim_sum
                                    break

            else:
                if nim_sum == 0:
                    ran1 = randint(0,len(self.stack)-1)
                    while not self.stack[ran1]:
                        ran1 = randint(0,len(self.stack)-1)
                    ran2 = randint(1,self.stack[ran1])
                    self.stack[ran1] -= ran2
                else:
                    for i in range(len(self.stack)):
                        if self.stack[i]^nim_sum < self.stack[i]:
                            self.stack[i] = self.stack[i]^nim_sum
                            break
        else:
            maxstack = max(self.stack)
            num_max = 0
            no_maxes = []
            for i in self.stack:
                if i == maxstack:
                    num_max += 1
                else:
                    no_maxes.append(i)
            if all([ i == 0 for i in no_maxes]):
                max_no_maxes = 0
                num_no_max = 0
            else:    
                max_no_maxes = max(no_maxes)
                num_no_max = 0
                for i in no_maxes:
                    if i == max_no_maxes:
                        num_no_max += 1
            if num_max == 1:
                if (num_no_max % 2) or not (num_no_max % 2) and self.master.misere == 0:
                    for i in range(len(self.stack)):
                        if self.stack[i] == maxstack:
                            self.stack[i] = max_no_maxes
                            break
                else:
                    for i in range(len(self.stack)):
                        if self.stack[i] == maxstack:
                            self.stack[i] = 0
                            break
            else:
                if self.master.misere:
                    if num_max % 2:
                        if num_no_max % 2:
                            for i in range(len(self.stack)):
                                if self.stack[i] == maxstack:
                                    self.stack[i] = 0
                                    break
                        else:
                            for i in range(len(self.stack)):
                                if self.stack[i] == maxstack:
                                    self.stack[i] = max_no_maxes
                                    break
                    else:
                        for i in range(len(self.stack)):
                            if self.stack[i] == maxstack:
                                self.stack[i] = 0
                                break
                else:
                    if num_max % 2:
                        for i in range(len(self.stack)):
                            if self.stack[i] == maxstack:
                                self.stack[i] = self.stack[i] - randint(1,self.stack[i])
                                break
                    else:
                        for i in range(len(self.stack)):
                            if self.stack[i] == maxstack:
                                self.stack[i] = 0
                                break


        for i in range(len(self.stack)):
            self.stackbuttons[i]["text"] = self.stack[i]
            if self.stack[i] == 0:
                self.stackbuttons[i]["state"]=DISABLED

    # computes label text
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
                if self.lastPlay:
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

    # call parent's quit method
    def quit(self):
        super().quit()


# widget that contains how we see the rules
class instructions(Nim):
    def __init__(self,master=None):
        super().callconstructor(master) # We call the frame constructor
        self.master = master #
        self.make_widgets()


    def make_widgets(self):
        self.menuButton = Button(self, cursor = "hand2", text="Back to menu", command=self.master.mainmenu, fg="blue")
        self.quitButton = Button(self, cursor = "hand2", text="Quit", command=self.quit,fg="red")
        self.rulesText = Text(self, width=50, height=20, wrap="word")
        # hardcoded text
        self.rulesText.insert('1.0', ('From Wikipedia: Nim is a mathematical game of strategy in which two players take '
            'turns removing objects from distinct heaps or piles. On each turn, a player must remove at least one object'
            ', and may remove any number of objects provided they all come from the same heap/pile. The goal of the game'
            ' is to be the player who removes the last object.\n\nIn our implementation of this game, players will take'
            ' turns removing objects from what we have called "stacks". There are two modes of play:\n  In Misere-mode t'
            'he object of the game is to avoid taking the last object from the last remaining stack. Taking the last obj'
            'ect will result in the player losing the game!\n  In Normal-mode, the player who takes the last object from'
            ' the last stack wins!\n\n In classic mode, there will be three stacks of randomly generated numbers, and th'
            'e player may take as many from whichever stack they prefer;\n In greedy mode, the player may only take obje'
            'cts from the stack with the largest number of objects remaining. \n Our custom option will allow the player'
            ' to choose how many stacks they would like to play with, from 1-9 stacks! We recommend playing with 1 stack'
            ' if you want to feel good about yourself!'))
        self.menuButton.grid(column=0, row=1)
        self.quitButton.grid(column=0, row=2)
        self.rulesText.grid(column=0, row=0)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

    def quit(self):
        super().quit()

# widget that displays the customization menu, similar to start widget
class diy(Nim):
    def __init__(self,master=None):
        super().callconstructor(master) # We call the grandparent constructor
        self.master = master # master is gonna be the parent instance
        self.stacknum= 0
        self.make_widgets()

    def make_widgets(self):
        # diy's children
        self.menuButton = Button(self, cursor = "hand2", text="Back to menu", command=self.master.mainmenu, fg="blue")
        self.quitButton = Button(self, cursor = "hand2", text="Quit", command=self.quit,fg="red")
        self.startButton = Button(self, cursor = "hand2", text="Start Game", command = self.master.play , fg="green")
        # settings frame, parent of the buttons that go in it, child of the diy widget
        self.sett = LabelFrame(self,text = "Customize your game",labelanchor ="n")
        # setting's children
        self.sett.empty0 = Frame(self.sett,width=20) #spacer
        self.sett.empty1 = Frame(self.sett,width=20) #spacer
        self.stacknum = IntVar() # control variable to be changed by the slider
        self.sett.slider = Scale(self.sett, variable=self.stacknum,from_= 1, to= 9,length=200,orient=HORIZONTAL, label="Number of stacks",command = self.change_stack)
        self.sett.vCPUbutton = Button(self.sett, cursor = "hand2", disabledforeground= "#999", text="1vCPU", command = lambda: self.mode_CPU(1))
        self.sett.vPbutton = Button(self.sett, cursor = "hand2", disabledforeground= "#999", text="1v1", command = lambda: self.mode_CPU(0))
        self.sett.mButton = Button(self.sett,cursor = "hand2", disabledforeground= "#999", text="misere", command = lambda: self.misere(1))
        self.sett.nButton = Button(self.sett,cursor = "hand2", disabledforeground= "#999", text="normal", command = lambda: self.misere(0))
        self.sett.clButton = Button(self.sett,cursor = "hand2", disabledforeground= "#999", text="classic", command = lambda: self.change_mode(0))
        self.sett.grButton = Button(self.sett,cursor = "hand2", disabledforeground= "#999", text="greedy", command = lambda: self.change_mode(1))
        # place widgets on screen
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
        self.master.stacknum = self.stacknum.get()

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

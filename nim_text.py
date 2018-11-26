# We're going object oriented here, so let's do this via a class called Game
import os

class Game():
    def __init__(self):
        self.stacks = []  # This is going to be where all the info in the game is
        self.running = True  # This controls the game loop
        self.turn = "Player 1"  # Who's turn is it? This might change to a different thing like a list
    def main(self):
        print("Welcome to Nim!")  # Welcome!
        n = -1  # initialize the loop to catch bad player behavior/PEBCAK error catching
        while not (n >= 3 and n <= 7):  # We can mess with this; these bounds define the range of how many stacks
            n = int(input("How many stacks? (choose 3-7, press enter) :"))
        for i in range(n):
            self.stacks.append((2*i)+1)  # classically it will be 2n+1, so 1, 3, 5, 7, etc, can alter this too
        while self.running:  # This is the game loop
            os.system('clear')   # clear a bunch of the terminal to make it less noisy
            print("Current stack values:")
            print('\n')
            for i in range(n):  # Remember how many stacks we made?
                print("Stack %d:  %d  left" % (i, self.stacks[i]))   # It puts 'em in like, a table-looking list
            print('\n')
            print("Current turn: ")
            print(self.turn)  # Which player's turn is it?
            print('\n'*2)
            s = -1  # iterate another PEBCAK controller
            while not (s >= 0 and s < n):  # This one exists to catch people trying to break the game, must pick valid stack!
                s = int(input("Take from which stack? : "))
                if self.stacks[s] == 0:
                    print("No pieces left in that stack! Try again!")
                    s = -1  # Try again!
            m = -1  # Once again, catching dumb people who are dumb
            while  not (m > 0 and m <= self.stacks[s]):
                m = int(input("How many? : "))
            self.stacks[s] -= m
            if all([ i == 0 for i in self.stacks ]):  # Basically, if every stack is empty, this conditional changes the flag to false and ends the game
                self.running = False
                break
                
            if self.turn == "Player 1":  # I want to change this, we can change it so that player 1 and player 2 enter their names or something cool like that
                self.turn = "Player 2"   # possibly using a dictionary or a list or something.
            else:
                self.turn = "Player 1"

        
        os.system('clear')

        print("No pieces left!")

        print("%s took the last piece! %s loses!" % (self.turn, self.turn))



if __name__ == '__main__':
    game = Game()
    game.main()


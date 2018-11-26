class Game():
    def __init__(self):
        self.stacks = []
        self.running = True
        self.turn = "Player 1"
    def main(self):
        print("Welcome to Nim!")
        n = -1
        while not (n >= 3 and n <= 7):
            n = int(input("How many stacks? (choose 3-7, press enter) :"))
        for i in range(n):
            self.stacks.append((2*i)+1)
        while self.running:
            print('\n'*5)
            print("Current stack values:")
            print('\n')
            for i in range(n):
                print("Stack %d:  %d  left" % (i, self.stacks[i]))
            print('\n')
            print("Current turn: ")
            print(self.turn)
            print('\n'*2)
            s = -1
            while not (s >= 0 and s < n):
                s = int(input("Take from which stack? : "))
                if self.stacks[s] == 0:
                    print("No pieces left in that stack! Try again!")
                    s = -1
            m = -1
            while  not (m > 0 and m <= self.stacks[s]):
                m = int(input("How many? : "))
            self.stacks[s] -= m
            if all([ i == 0 for i in self.stacks ]):
                self.running = False
                break
                
            if self.turn == "Player 1":
                self.turn = "Player 2"
            else:
                self.turn = "Player 1"

        
        print('\n'*5)

        print("No pieces left!")

        print("%s took the last piece! %s loses!" % (self.turn, self.turn))



if __name__ == '__main__':
    game = Game()
    game.main()


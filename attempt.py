class daddy:
    def __init__(self):
        #instance attributes
        self.mode = 1
        self.type = "sugar daddy"
        self.baby = baby(self) # creates an instance of its child.
    def givesugar(self):
        self.name = "best daddy"
        print("sugar given")

class baby(daddy):
    def __init__(self, master = None):
        self.master = master
        # this is how you change the parent's attribute
        self.master.mode = 7
        # you can change the parent instance attribute like this
        self.master.name = "pervy daddy"
        # this is how a child changes its own attribute without affecting the parent
        self.mode = 5
        self.master.givesugar()

app = daddy()
print(app.mode) # outputs 7
print (app.name) # outputs pervy daddy
app.mode= 3
print (app.mode) # outputs 3
print (app.baby.mode) #outputs 5
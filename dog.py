# Python OPP

class Dog:
    owner = "Mina" #-----> class attributte 
    def __init__(self, name, breed, weight, energy = 100, happiness = 30):
        self.name = name 
        self.breed = breed
        self.weight = weight 
        self.energy = energy 
        self.happiness = happiness

    def speak(self): #----> methods
        print("Woof!") 

    def run(self):
        print("I am running")
    
    def bite(self):
        print("I am biting")
    
    def drop(self):
        print("I am dropping")

    def fetch(self):
        if self.energy > 75:
            self.run()
            self.bite()
            self.run()
            self.drop()
            self.speak()

            self.energy -= 75
            self.happiness += 25
        else:
            print("I am too tired ")
        

spot = Dog('spot','lab', 200)
bill = Dog('bill','golden',210)

#EXAMPLES: NOTICE THE DIFFERENT!
# print(spot.energy) ----> notice that here we are printing.
# spot.speak() ----> notice that here we are using a function.
# spot.bite()
# print(bill.happiness)

spot.fetch()
spot.fetch()
# print(spot.energy)
# print(spot.happiness)
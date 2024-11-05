#A class named Car with make,model and year.
#A method called display_info() that prints car details
#An instance of the class

#CLASS CREATION
class Car:
    #CONSTRUCTOR
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    #METHOD
    def display_info(self):
        print(f"I will own a {self.make} {self.model} {self.year}")
        return "Nice car"
#INSTANCE
Gari=Car("Lexus","L300","2022")
print(Gari.display_info())
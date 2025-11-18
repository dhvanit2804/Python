'Create a class Car with brand, model, and year. Add a method to display full details.'

class Car:
    def __init__(self, brand, model, year):
        self.b = brand
        self.m = model
        self.y = year

    def showdetails(self):
        print(f"Car Brand: {self.b}")
        print(f"Car Model: {self.m}")
        print(f"Car Year: {self.y}")

c = Car("Toyota", "Fortuner", 2020)

c.showdetails()
'Create a class Vehicle and a derived class Bike. Add a method in Bike to print special features.'

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def show_details(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")

class Bike(Vehicle):
    def special_features(self):
        print("Special Features:")
        print("- Lightweight body")
        print("- Best for city rides")
        print("- High mileage")

b = Bike("Honda", "Shine")

b.show_details()
b.special_features()

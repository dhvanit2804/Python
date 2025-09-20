'''Create a class 'Pets' from a class 'Animals' and further create a class 'Dog' from 
'Pets'. Add a method 'bark' to class 'Dog'. '''

class Animal:
    pass

class pets(Animal):
    pass

class Dog(pets):

    @staticmethod
    def bark():
        print("Bow Bow!")

d = Dog()
d.bark()
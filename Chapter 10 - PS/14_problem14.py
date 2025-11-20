'Create a class Book with private attribute __price. Add getters and setters.'

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.__price = price

    def get_price(self):
        return self.__price

    def set_price(self, price):
        if price >= 0:
            self.__price = price
        else:
            print("Price cannot be negative.")

b = Book("1984", "George Orwell", 300)
print(f"Book: {b.title} by {b.author} | Price: ₹{b.get_price()}")
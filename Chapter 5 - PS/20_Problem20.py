'''Implement a simple Contact Book using dictionary:
Add contact
Search contact
Delete contact'''

contact_book = {}
def add_contact(name, phone):
    contact_book[name] = phone
    print(f"Contact {name} added.")

def search_contact(name):
    if name in contact_book:
        print(f"{name}: {contact_book[name]}")
    else:
        print(f"Contact {name} not found.")

def delete_contact(name):
    if name in contact_book:
        del contact_book[name]
        print(f"Contact {name} deleted.")
    else:
        print(f"Contact {name} not found.")

# Example usage:
add_contact("Alice", "123456789")
add_contact("Bob", "987654321")
search_contact("Alice")
delete_contact("Bob")
search_contact("Bob")

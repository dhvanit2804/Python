'Write a function to generate a multiplication table of any number.'

def multiplication_table(num):
    for i in range(1, 11):
        print(f"{num} x {i} = {num*i}")


print(multiplication_table(7))
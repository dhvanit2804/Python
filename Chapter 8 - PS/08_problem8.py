'Write a python function to print multiplication table of a given number.'

def mutiplication(n):
    for i in range(1, 11):
        print(f"{n} X {i} = {n*i}")

mutiplication(7)
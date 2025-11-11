'Take 5 inputs from the user and store them in a list.'

l = []

for i in range(5):
    element = input(f'Enter element {i+1}: ')
    l.append(element)
    print(f'List after adding element {i+1}: {l}')
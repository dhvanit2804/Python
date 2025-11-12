'What is Type Defination in Python ?'
'# Type Defination in Python is a way to specify the expected data types of variables, function parameters, and return values.'
'# It helps in improving code readability and maintainability.'

from typing import List, Tuple, Dict, Union
n : int = 5
name : str = "Dhvanit"

print(type(n))
print(type(name))

def sum(a: int, b: int) -> int:
    return a + b

print(sum(50, 70))
'What is Walrus Operator ?# The Walrus Operator is a new operator introduced in Python 3.8.'
# It is also known as the assignment expression operator.
# It is denoted by :=
# The Walrus Operator allows you to assign a value to a variable within an expression.

if (n := len([1, 2, 3, 4, 5])) > 3: 
    print(f"List is too long ({n} elements, expected <= 3)")
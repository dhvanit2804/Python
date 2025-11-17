'''Write a function to calculate simple interest.
(formula: SI = (P × R × T) / 100)'''

def s(p, r, t):
    formula = (p*r*t) / 100
    return formula

print(s(10, 20, 30))
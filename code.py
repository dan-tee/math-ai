from sympy import * 
from sympy import symbols, Eq, solve

def find_n():
    n = symbols('n')
    equation = Eq((1/4)*(1 - (1/2)**n)/(1 - 1/2), 63/128)
    solution = solve(equation, n)
    return solution

result = find_n()
print(result)

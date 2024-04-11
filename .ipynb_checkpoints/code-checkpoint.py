from sympy import * 
from sympy import symbols, simplify

def calculate_distance_squared_sum():
    l = symbols('l')
    k = (l + 4) / 9
    distance_squared_sum = 2 * (122 * k**2 - 12 * k + 32)
    distance_squared_sum_mod_1000 = simplify(distance_squared_sum) % 1000
    return distance_squared_sum_mod_1000

result = calculate_distance_squared_sum()
print(result)

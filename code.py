from sympy import * 
from sympy import symbols, solve, N

def sum_of_distances_intersection_points():
    """Problem: Let $\mathcal{P}$ be the parabola in the plane determined by the equation $y = x^2.$  Suppose a circle $\mathcal{C}$ intersects $\mathcal{P}$ at four distinct points.  If three of these points are $(-28,784),$ $(-2,4),$ and $(13,169),$ find the sum of the distances from the focus of $\mathcal{P}$ to all four of the intersection points.
"""
    x, y = symbols('x y', real=True)

    # The focus of the parabola y = x^2 is at (0, 1/4)
    focus_x, focus_y = 0, 1/4

    # The given intersection points
    points = [(-28, 784), (-2, 4), (13, 169)]

    # The sum of the distances from the focus to the intersection points
    sum_of_distances = 0
    for point in points:
        # Calculate the distance using the distance formula
        sum_of_distances += ((focus_x - point[0])**2 + (focus_y - point[1])**2)**0.5

    # Convert the sum of distances to decimal
    sum_of_distances = N(sum_of_distances)

    return sum_of_distances

result = sum_of_distances_intersection_points()
print(result)

"""
HW01 by Zach George
In this assignment, a user enters three values for sides of a triangle
Outputs the classification of the triangle based off of the entered sides,
or outputs that the side is not valid due to the value not being an integer.
"""

def classify_triangle(side_a: int, side_b: int, side_c: int) -> str:

    """ Given sides a, b, and c, return what kind of triangle it is """

    if not isinstance(side_a,int) or not isinstance(side_b, int) or not isinstance(side_c, int):
        raise TypeError('At least one of the sides is not an integer.')

    if int(side_a) <= 0 or int(side_b) <= 0 or int(side_c) <= 0:
        raise ValueError('The sides must be greater than 0.')

    #sort inputs so largest value is last
    side_a, side_b, side_c = tuple(sorted([side_a,side_b,side_c]))
    outputted_triangle: str = ''
    if side_a == side_b and side_b == side_c:
        outputted_triangle = 'Equilateral'
    elif side_a == side_b or side_b == side_c or side_a == side_c:
        outputted_triangle = 'Isosceles'
    elif sum([int(side_a) ** 2, int(side_b) ** 2]) == int(side_c) ** 2:
        outputted_triangle = 'Scalene and Right'
    else:
        outputted_triangle = 'Scalene'

    #return triangle type
    return outputted_triangle

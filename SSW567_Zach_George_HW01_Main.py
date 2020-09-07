"""
HW01 by Zach George
In this assignment, a user enters three values for sides of a triangle
Outputs the classification of the triangle based off of the entered sides,
or outputs that the side is not valid due to the value not being an integer.
"""

from typing import List, Tuple

def classify_triangle(a: int, b: int, c: int) -> str:

    """ Given sides a, b, and c, return what kind of triangle it is """
    
    if type(a) is not int or type(b) is not int or type(c) is not int:
        raise TypeError('At least one of the sides is not an integer.')
    elif int(a) <= 0 or int(b) <= 0 or int(c) <= 0:
        raise ValueError('The sides must be greater than 0.')
    else:
        if a == b and b == c:
            return 'Equilateral'
        elif a == b or b == c or a == c:
            return 'Isosceles'
        elif sum([int(a) ** 2, int(b) ** 2]) == int(c) ** 2:
            return 'Scalene and Right'
        else:
            return 'Scalene'

def main() -> None:

    """ Ask user for sides a, b, c """

    sides: List(int) = list()

    for i in range(len(['a', 'b', 'c'])):
        try:
            sides.append(int(input('Please enter the integer value for side ' + str(['a', 'b', 'c'][i]) + ": ")))
        except ValueError:
            raise ValueError('Input is not an integer.')

    print(classify_triangle(sides[0], sides[1], sides[2]))


if __name__ == "__main__":
    main()
"""
Automated tests used to test the classify triangle function 
Experience with assignment:
The challenges I had with this assignment are what code was needed to check if the inputs are of the right type.
I am sure there is a different (and better) way than I did it, but this is the way that worked for me.
I thought the requirements specification for this assignment was overall was basic, even for what is needed.
There is other criteria that makes a triangle a triangle (i.e. sum of two sides must be greater than the third side).
It did not indicate which types of inputs are allowed. Integers and floats are both technically allowed, but is there a specific type that is being requested?
Additionally, it did not indicate how the string is formatted when outputted. 
I did not encounter a lot of difficulty with the tools, as I took SSW-810 over the summer. Unittest is pretty fresh in my mind.
Based off of the present problem being solved, there were two criterion that needed to be met. 
First, the inputs must be integers (I chose integers for this assignment)
Second, the inputs all must be greater than 0. 
For the first criteria, I tested some other types of inputs to ensure I was done (str, bool, float)
For the second criteria, I tested one where one of the sides was 0 and another where one was less than 0.
I only chose one side to have as one of these values for both criterion, since testing all three inputs at the same time would be unnecessary. 
Based off of the criteria, these are sufficient test cases. 
"""

import unittest
from ssw567_zach_george_hw01_main import classify_triangle


class ClassifyTriangleTest(unittest.TestCase):
    

    """ Define the unittest class for the clarify triangle function """

    def test_classify_triangle_errors(self) -> None:

        """ Test the classify triangle function """

        with self.assertRaises(TypeError):
            classify_triangle(1, 2, True)
        with self.assertRaises(TypeError):
            classify_triangle(1, 2, 4.5)
        with self.assertRaises(TypeError):
            classify_triangle('one', 2, 4)
        with self.assertRaises(ValueError):
            classify_triangle(0, 1, 2)
        with self.assertRaises(ValueError):
            classify_triangle(3, -4, 2)

    def test_classify_triangle_outputs(self) -> None:
    
        self.assertEqual('Equilateral', classify_triangle(4, 4, 4))
        self.assertEqual('Isosceles', classify_triangle(4, 4, 6))
        self.assertEqual('Scalene and Right', classify_triangle(3, 4, 5))
        self.assertEqual('Scalene', classify_triangle(4, 8, 10))

if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)


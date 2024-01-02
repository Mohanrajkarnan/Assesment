#To learn unit tests 

#1 : Import the necessary modules (unittest)
#2 : Create test cases (unittest.TestCase)
#3 : Write Test methods (assertEqual(),assertTrue() or assertFalse())
#4 : Run the tests : unittest.main()


import unittest
import logging

def multiply(a,b):
    """
    This method will retrun multipy of two numbers.
    """
    try:
        return a*b
    except Exception as e:
        print("This is the error : {e}")

#Algebra 

#Multiplication uses a Algebra fact (Commutative fact)
# A positive times a negative is always a negative 
# Negative times a negative is positive 

class TestMultiplication(unittest.TestCase):
    """
    Unit test for multiplication function
    """
    def testMulPos(self):
        result = multiply(3,4)
        self.assertEqual(result,12)
        print("testMulPos passed")

    def testMulNeg(self):
        result = multiply(-5,2)
        self.assertEqual(result,-10)
        print("testMulNeg passed")


    def testMulNeg01(self):
        result = multiply(3,0)
        self.assertEqual(result,0)
        print("testMulNeg01 passed")

if __name__ == "__main__":
    unittest.main()
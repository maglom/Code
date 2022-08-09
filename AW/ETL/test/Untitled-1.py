
"""
Exercise:
1. Write at least one unit test for each method of the Calculator class.
   Afterwards, run `coverage run -m unittest 000_testing.py`, then run `coverage 
report` to see the test coverage. 
2. The div method in the Calculator class is poorly implemented. If we divide by 
zero, we will get an error.
   Most calculators return "inf" when dividing by zero, so ours should do that as 
well.
   First, try using the calculator class to divide by zero and see what error you 
get.
   Then, write a test that gives the behaviour that we want (i.e that when you 
divide by zero you get "inf" back)
   Try running the test now. It should fail since we haven't implemented the fix 
yet.
   After seeing it fail, fix the div method so that the test passes.
  
"""
import unittest
class Calculator:
    """
    The calculator class can be used like this:
    calc = Calculator()
    result = calc.add(1,2)
    print(result) => prints 3
    """
    def add(self, a, b):
        return a+b
    def sub(self, a, b):
        return a-b
    def mul(self, a, b):
        return a*b
    def div(self, a, b):
        return a/b
class CalculatorTest(unittest.TestCase):
    # The method name should describe what the test does 
    def test_example(self):
        # Write your test case here
        self.assertEqual(True, False)
    # Write more test methods here
     
class CalculatorTest(unittest.TestCase):
    # The method name should describe what the test does 
    def test_add(self):
        #Given
        a, b = 1, 2
        #When
        calc = Calculator()
        res = calc.add(a, b)
        #Then
        self.assertEqual(3, res, 'Result should be a + b')
    def test_sub(self):
        #Given
        a, b = 2, 1
        #When
        calc = Calculator()
        res = calc.sub(2,1)
        #Then
        self.assertEqual(1, res, 'result should be a - b')
    def test_mul(self):
        #Given
        a, b = 1, 2
        #when
        calc = Calculator()
        res = calc.mul(a,b)
        #Then
        self.assertEqual(res, a*b, 'result should be a * b')
    def test_div(self):
        #Given
        a, b = 1, 2
        #when
        calc = Calculator()
        res = calc.div(a,b)
        #Then
        self.assertEqual(res, a/b, 'result should be a / b')
        
calc = Calculator()
calc.div(5,0)
    
if __name__ == '__main__':
   unittest.main()

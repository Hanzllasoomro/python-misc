import pdb
import unittest

class Calculator:
    def add(self, a, b):
        pdb.set_trace()
        result = a + b
        return result
    def subtract(self, a, b):
        pdb.set_trace()
        result = a - b
        return result
    def multiply(self, a, b):
        pdb.set_trace()
        result = a * b
        return result
    def divide(self, a, b):
        pdb.set_trace()
        if b == 0:
            raise ZeroDivisionError
        result = a / b
        return result
    def power(self, a, b):
        pdb.set_trace()
        result = a ** b
        return result

class TestSum(unittest.TestCase):
    cal = Calculator()
    def test_add(self):
        self.assertEqual(self.cal.add(1, 2), 3)
    def test_subtract(self):
        self.assertEqual(self.cal.subtract(3, 2), 1)
    def test_multiply(self):
        self.assertEqual(self.cal.multiply(2, 2), 4)
    def test_divide(self):
        self.assertEqual(self.cal.divide(4, 2), 2)
    def test_power(self):
        self.assertEqual(self.cal.power(2, 2), 4)

if __name__ == '__main__':
    unittest.main()
    ### ---- OUTPUT ----
# Testing started at 2:35 PM ...
# Launching unittests with arguments python -m unittest E:\python\Module 2\exercise1.py in E:\python\Module 2
#
# > e:\python\module 2\exercise1.py(6)add()
# -> pdb.set_trace()
# (Pdb) > n
# -> result = a + b
# (Pdb) > n
# -> return result
# (Pdb) p result
# (Pdb) 3
# (Pdb) > e:\python\module 2\exercise1.py(18)divide()
# -> pdb.set_trace()
# (Pdb) > n
# -> if b == 0:
# (Pdb) p b
# (Pdb) 2
# (Pdb) > n 
# -> result = a / b
# (Pdb) > e:\python\module 2\exercise1.py(22)divide()
# -> return result
# (Pdb) 2.0
# (Pdb) > e:\python\module 2\exercise1.py(14)multiply()
# -> pdb.set_trace()
# (Pdb) > e:\python\module 2\exercise1.py(15)multiply()
# -> result = a * b
# (Pdb) p a
# (Pdb) 2
# (Pdb) p b
# (Pdb) 2
# (Pdb) > e:\python\module 2\exercise1.py(16)multiply()
# -> return result
# (Pdb) 4
# (Pdb) > e:\python\module 2\exercise1.py(24)power()
# -> pdb.set_trace()
# (Pdb) > e:\python\module 2\exercise1.py(25)power()
# -> result = a ** b
# (Pdb) 2
# (Pdb) 2
# (Pdb) > e:\python\module 2\exercise1.py(26)power()
# -> return result
# (Pdb) 4
# (Pdb) > e:\python\module 2\exercise1.py(10)subtract()
# -> pdb.set_trace()
# (Pdb) > e:\python\module 2\exercise1.py(11)subtract()
# -> result = a - b
# (Pdb) 3
# (Pdb) 2
# (Pdb) > e:\python\module 2\exercise1.py(12)subtract()
# -> return result
# (Pdb) 1
# (Pdb)
#
# Ran 5 tests in 81.155s
#
# OK

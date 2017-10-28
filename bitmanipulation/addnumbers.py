"""
Problem: 
Add two numbers without using +, - operators

Algorithm: 
we use bitwise operators : & and ^

In every iteration: 
a & b gives us bits we have to carry left 
a ^ b adds individual bits 0 ^ 0 and 1 ^ 1 = 0 while 0 ^ 1 and 1 ^ 0 = 1
move carry bits left by 1  
"""

print(__doc__)

class SolutionSum(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        # Required in Python to support negative numbers 
        MAX_BIT = 2**32
        MAX_BIT_COMPLIMENT = -2**32
        
        while b != 0:
            # Required in Python to support negative numbers. 
            if b == MAX_BIT: 
                return a ^ MAX_BIT_COMPLIMENT
            # Get carry bits
            carry = a & b
            # Or to get addition across bits 
            a = a ^ b
            # move carry bits left 
            b = carry << 1
        
        return a 
    
if __name__ == '__main__':
    s = SolutionSum()
    print(s.getSum(10, 12))
    print(s.getSum(-10, -13))
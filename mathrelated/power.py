class SolutionPower(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        
        res = 1
        is_negative = True if n < 0 else False 
        n = abs(n)
        
        while n != 0: 
            if n & 1:
                res *= x
            x *= x 
            n >>= 1
        
        return 1 / res if is_negative else res
    
if __name__ == '__main__':
    s = SolutionPower()
    print(s.myPow(1.454, 5))
    print(s.myPow(27, -3))
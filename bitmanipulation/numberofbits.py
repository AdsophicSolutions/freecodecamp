"""
Problem: 
Count number of set bits in an integer 

Algorithm: 
1. Initialize and_value variable to 1 << 31. 
2. perform and_value & n.
3. result is non-zero if bit 32 is set. Add 1 to number of bits if set else add 0 
4. shift and_value one bit right. 
5. repeat steps from 2 to 5 till and_value is 0 
"""
print(__doc__)

class SolutionCountBits(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Init and_value 
        and_value = 1 << 31
        num_of_bits = 0
        while and_value != 0:
            # if bit is set increment number of set bits by 1  
            num_of_bits += (1 if n & and_value else 0)
            # right shift and_value by 1 
            and_value >>= 1
        
        return num_of_bits
    
if __name__ == '__main__':
    s = SolutionCountBits()
    print(s.hammingWeight(10012423))
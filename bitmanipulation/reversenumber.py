"""
Problem: 
Reverse bits of a 32-bit number. Means if bit 32 in original number is 1 then bit 1 
in reversed number is 1. If bit 31 is 0 in original number is 0 then bit 2 in new 
number is 0.. and so on. 

Algorithm: 
1. Init res = 0 and and_num = 1.
2. Shift res left and  
3. Perform n & and_num and |= with res to set next bit
4. Shift and_num left to compare against next number  
5. Repeat steps from 2 to 5 
"""

print(__doc__)

class SolutionReverseBits:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        # Init 
        res = 0 
        and_num = 1 
        end_sum = 1 << 31
        while and_num <= end_sum:
            # Shift res left 
            res <<= 1
            # Or res with and_num and n to determine 
            # if res bit should be set
            res |= (1 if and_num & n else 0)            
            and_num <<= 1
        
#         res |= (1 if and_num & n else 0)
        return res
     

def print_bits(n):
    output = []
    and_num = 1 << 31
    while and_num != 0:
        output.append('1' if and_num & n else '0')
        and_num >>= 1
    
    print ("{0} ({1})".format(n, "".join(output))) 
    
if __name__ == '__main__':
    s = SolutionReverseBits()
    n = 1 
    print_bits(n)    
    res = s.reverseBits(n)
    print_bits(res)
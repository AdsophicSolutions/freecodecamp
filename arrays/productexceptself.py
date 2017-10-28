"""
Problem: 
Given an array, return an array which at a particular index returns product of all other numbers in the original array other than itself 

Algorithm & Solution: 
Explanation is quite simple and best explained through code comments. Please look below 

Time Complexity: O(n)
Space Complexity: O(n) 
"""
print(__doc__)

class SolutionProductExceptSelf(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        Big O is O(n) for this algorithm 
        """
        if not nums or len(nums) == 1:
            return nums 
        
        # Create new array to hold results
        output = [0] * len(nums)
        
        result = 1
        # For input array [3, 4, 5] 
        # output will look like [1, 3, 12]
        # at the end of this loop. Notice how last element already has the
        # right result and first element has 1
        for i in range(len(nums)):
            output[i] = result 
            result *= nums[i]
        
        result = 1
        # Now iterate from right to left 
        # Now output will look like [20, 15, 12]
        # result we are looking for  
        for i in reversed(range(len(nums))):
            output[i] *= result 
            result *= nums[i]
        
        return output

if __name__ == '__main__':
    s = SolutionProductExceptSelf()
    array = [3, 4, 5]
    print("Input= {}".format(array))
    print("Result= {}".format(s.productExceptSelf(array)))
    print() 
    array = [2,3,1,4]
    print("Input= {}".format(array))
    print("Result= {}".format(s.productExceptSelf(array)))
    
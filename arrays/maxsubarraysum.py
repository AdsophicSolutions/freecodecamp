"""
Problem: 
Given an array return maximum sub-array sum. Array contains integers 

Algorithm & Solution: 
Important concept to grasp here is while traversing the array if value for a particular element is greater running sum of elements before it + element value, we can make value of this element the running sum. Let's consider an example:
 
-3 -2 1 are first three elements of an array
when we arrive at index 2 (element value 1) our running sum is -5. If we add 1 to our running sum our new running_sum becomes -4. The other option is to make 1 our new running sum. We must choose the second option because any subsequent running_sum will be greater if we start with 1 instead of -4. 

Now that we know what to use as the running sum, we just need to keep track of a max_sum, which is the largest running sum so far.  

Time Complexity: O(n) 
Space Complexity: O(1)
"""
import itertools
from functools import reduce  

print(__doc__)

class SolutionMaxSubArray(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0 
                
        max_sum = running_sum = nums[0]
        
        for num in itertools.islice(nums, 1, None):
            # if running_sum
            running_sum = max(running_sum + num, num)
              
            # if running sum running_sum > max_sum we have found
            # a new max_sum 
            max_sum = max(max_sum, running_sum)
        
        return max_sum 
    
    def maxSubArrayReduce(self, nums):
        """
        Advanced method 
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0 
        
        # Demonstration of reduce could be used to perform the same 
        # function
        return reduce(lambda max_t, num: (
            max(max_t[0] + num, num), 
            max(max_t[1], max(max_t[0] + num, num))), 
                      itertools.islice(nums, 1, None), (nums[0], nums[0]))[1]
    
if __name__ == '__main__':
    s = SolutionMaxSubArray()    
    array = [1, 2, 3, 4]
    print("Input= {}".format(array))    
    print("Answer= {}".format(s.maxSubArray(array)))
    print("Answer= {}".format(s.maxSubArrayReduce(array)))
    print() 
    array = [-2,1,-3,4,-1,2,1,-5,4]
    print("Input= {}".format(array))    
    print("Answer= {}".format(s.maxSubArray(array)))
    print("Answer= {}".format(s.maxSubArrayReduce(array)))
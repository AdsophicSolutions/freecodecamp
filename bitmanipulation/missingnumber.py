"""
Problem: 
In an unsorted list of numbers beginning from 0 return the first missing number. 
Operation must be completed in O(n) time complexity and O(1) space complexity 

Algorithm: 
Solution involves using the list itself as a hash table to mark numbers found. We negate the value at 
the index denoted by a value in the list. 
For example: Consider list [1, 2, 3]. when we encounter value 1 we negate 2 to -2, since it is the value at 
index 1.  If number found is larger than the list size we ignore the value. We make one passing updating the list 
List at the end of the pass will look like [1, -2, -3]. 
In the second iteration we look for the first number that is still positive. The index signifies missing integer, in this 
example that integer is 0

IMPORTANT: 
1. Since list can contain 0 and negative of 0 is 0, we first increment each number by 1. 
2. When iterating through the list, we must take absolute of list value. It could be negated. 
3. We do not negated a number if it is already negated 
"""

print(__doc__)

class SolutionMissingNumber(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: 
            return 0 
        
        # Increment all elements by 1 
        for i in range(len(nums)):
            nums[i] += 1
        
        # Negate values at index based on values    
        for i in range(len(nums)):
            # Take abs of value since it could be negated
            hash_val = abs(nums[i]) - 1
            # Only negate number if number less than list size 
            # and it has not already been negated
            if hash_val < len(nums) and nums[hash_val] > 0:
                nums[hash_val] *= -1
                    
        # return first positive number
        for i in range(len(nums)):
            if nums[i] > 0:
                return i 
        
        # No positives found. First missing number is len(nums)
        return len(nums)

if __name__ == '__main__':
    s = SolutionMissingNumber()
    print(s.missingNumber([0,1,3]))
    print(s.missingNumber([2,3]))
    print(s.missingNumber([4,3,0,2,1,6]))
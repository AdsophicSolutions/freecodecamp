"""
Problem: 
Given a list of number return unique combination subsets. 
Example: 
Input: [1, 2, 2]
Answer: [[], [1, 2], [1], [1, 2, 2], [2], [2, 2]] 

Algorithm: 
We use recursion. In an outside loop we call combinations method with 
our list and length of the current combination. Recurse till we reach 
length of combination we want. We add combination to set (set consist of 
unique elements) Increment outside loop by 1 and repeat
"""
print(__doc__)

class SolutionCombinationsNoDups(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return nums
        
        # declare set as output. 
        # Set automatically maintains 
        # a unique set 
        output = set()      
          
        #recursive function 
        def combinations(nums, length, comb):            
            if length == 0:
                comb.sort()
                # Add to output. Set  
                # maintains a single copy
                output.add(tuple(comb))
                return
            
            # Iterating till last element is not necessary 
            # for length more than one, since combination 
            # of size cannot be constructed. 
            for i in range(len(nums) - length + 1):
                # recurse for remaining elements, reduced length, old combination + current element                
                combinations(nums[i + 1:], length - 1, comb[:] + [nums[i]])
        
        # outside loop for initializing size of combination
        for i in range(len(nums) + 1):
            combinations(nums, i, [])
        
        # convert unique set to lists and return    
        return [list(c) for c in output]

if __name__ == '__main__':
    num_list = [1, 2, 2]
    print("Input")
    print(num_list)
    print("Answer")
    s = SolutionCombinationsNoDups()
    print(s.subsetsWithDup(num_list))
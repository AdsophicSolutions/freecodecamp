"""
Problem: 
Given a list of number return all combination subsets. 
Example: 
Input: [1, 2, 3]
Answer: [] [1] [2] [3] [1, 2] [1, 3] [2, 3] [1, 2, 3] 

Algorithm: 
We use recursion. In an outside loop we call combinations method with 
our list and length of the current combination. Recurse till we reach 
length of combination we want. Increment outside loop by 1 and repeat

"""
print (__doc__)

class SolutionCombinations(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return nums
        
        output = []
        output.append([])
        
        # recursive function
        def combinations(nums, length, comb):
            # if we've reached combination length
            # add combination and return 
            if length == 0:
                output.append(comb)
                return
            
            # NOTE: we only need to perform this for len(nums) - length times 
            for i in range(len(nums) - length + 1):     
                # remove first element, reduce length by 1, add current element to combination            
                combinations(nums[i + 1:], length - 1, comb[:] + [nums[i]])
        
        # Outside loop to setup combination size. 
        for i in range(1, len(nums) + 1):
            combinations(nums, i, [])
            
        return output
    
if __name__ == '__main__':
    s = SolutionCombinations()
    input_list = [1, 2, 3]
    print("Input:")
    print(input_list)
    print("Answer:")
    print(s.subsets(input_list))
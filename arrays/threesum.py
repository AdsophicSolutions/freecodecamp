"""
Problem: 
Given a list of integers return unique set of 3 numbers that add up to 0. 
Example: 
[-1, 0, 1, 2]
[-1, 0 ,1]

Algorithm:
We want to improve on brute force algorithm which is calculating sum of every possible combination of numbers and picking unique combinations that sum to 0. Time complexity is O(n ^ 3). 

Our solution
1. Sort list (O(n * log n)) 
2. Iterate through list 
3. For each integer in list
    - Start by picking next integer (variable si) and last integer in another loop (variable ei)
    - if sum of the three is equal to 0 add to unique set. Increment si, Decrement ei  
    - if sum < 0 increment si since list is sorted. 
    - if sum > 0 decrement ei since list is sorted. 
    - Run this loop while si < ei 

After sort our algorithm runs in O(n ^ 2) time. 
Additional optimizations: 
1. In first iteration if value exceeds 0 we can break. Since every integer after is >= current integer sum will also exceed 0. 
2. If sum of value at current integer and value of si > 0 we can move to next number. Value of integer at ei >= so sum of three numbers will also be > 0. 
3. We are only interested in unique sets. If integer at index is equal to previous index any combination for that integer value is already covered. Continue to next integer

Time Complexity: O(n * log n) + O(n ^ 2) 
Space Complexity: O(1) - excluding output unique set
"""

print(__doc__)

class SolutionThreeSum():    
    def threeSum(self, nums):
        if not nums or len(nums) < 3:
            return []
        
        nums.sort() 
        unique_set = set() 
        # Iterate through list. range excludes last two integers
        # since our solution set is 3 numbers.  
        for i in range(len(nums) - 2):
            # Since array is sorted if nums value > 0 
            # any other subsequent numbers will sum with also be > 0             
            if nums[i] > 0:
                break
            
            # For if current number is equal to previous number we don't 
            # all unique sets for the number are already covered. 
            if i != 0 and nums[i] == nums[i - 1]: 
                continue 
            
            # Init si and ei
            si = i + 1;
            ei = len(nums) - 1
            while si < ei:
                # if just the aggregate of the first two numbers is greater 
                # than 0, we can proceed to next number  
                if nums[i] + nums[si] > 0: 
                    break
                
                num_sum = nums[i] + nums[si] + nums[ei]
                if num_sum == 0:
                    # NOTE: For those unfamiliar with Python sets 
                    # duplicate check is unnecessary. 
                    unique_set.add((nums[i], nums[si], nums[ei]))
                     
                    # sum is equal so increment si and decrement ei
                    si += 1 
                    ei -= 1
                # if num_sum > 0, decrement ei by 1
                elif num_sum > 0: 
                    ei -= 1
                # num_sum < 0 increment si by 1 
                else: 
                    si += 1
        
        return [list(t) for t in unique_set] 

if __name__ == '__main__':
    s = SolutionThreeSum()
    
    array = [-1, 0, 1, 2, -1, -4]
    print("Input: Array = {}".format(array))
    print("Answer: Unique combinations = {}".format(s.threeSum(array)))
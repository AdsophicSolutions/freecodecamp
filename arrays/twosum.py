'''
Problem: 
Given an array of integers return indices of two elements that sum to a given sum. 

Algorithm: 
We are looking to improve on brute force algorithm which is calculating sum for all combinations of integers and involves O(n ^ 2) time complexity

Solution: 
Key to solving this problem is iterating through nums and checking for existence of (target - current num value). We store each number encountered and its corresponding index in a dictionary and continue to iterate. If we encounter another number such that dictionary contains (target - num) return index for the number from the dictionary and index of current numbers. If no match is found return empty list 

Time Complexity: O(n) 
Space Complexity: O(n)   
'''
print(__doc__) 

class SolutionTwoSum(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]        
        """
        # Create dicctionary 
        calc = {}
        
        for i, n in enumerate(nums):
            # check if target - n exists. return if found  
            if target - n in calc:
                return [calc[target - n], i]
                        
            # set current nums index at index n in cache. 
            if n not in calc: 
                calc[n] = i
        
        return []

if __name__ == '__main__':
    s = SolutionTwoSum()
    array = [4,5,7,2,5,3,1,9]
    target = 10 
    print("Input:")
    print("List: {} Target: {}".format(array, target))
    print("Answer: {}".format(s.twoSum(array, target)))
    
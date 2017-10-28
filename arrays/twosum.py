'''
Problem: 
Given an array of integers return indices of two elements that sum to a given sum. 
Input assumptions: 
1. Values in input >= 0. 
2. All input values < target value

Algorithm: 
We are looking to improve on brute force algorithm which is calculating sum for all 
combinations of integers and involves O(n ^ 2) time complexity

Solution: 
Algorithm runs in O(n) time. Key to solving this problem is iterating through nums 
and checking for existence of (target - current num value). We do this by declaring 
another array of size target (calc) initialized to all -1 and setting value at 
calc index of element value to index of element. Example: if input array contains 
value 4 at index 2 (nums[2] = 4), we set calc[4] = 2

For supporting input arrays with negative values or values exceeding target create a calc dictionary 
instead of array.

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
        # Create a cache size of target 
        calc = [-1] * target
        r_list = []
        
        for i, n in enumerate(nums):
            # check index target - n. If index exists we've found a match!! 
            if calc[target - n] != -1:
                r_list.append(calc[target-n])
                r_list.append(i)
                break
                        
            # set current nums index at index n in cache. 
            if calc[n] == -1: 
                calc[n] = i 
        
        return r_list

if __name__ == '__main__':
    s = SolutionTwoSum()
    array = [4,5,7,2,5,3,1,9]
    target = 10 
    print("Input:")
    print("List: {} Target: {}".format(array, target))
    print("Answer:")
    print(s.twoSum(array, target))
    
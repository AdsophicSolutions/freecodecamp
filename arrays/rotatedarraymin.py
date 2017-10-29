"""
Problem: 
Given an pivoted sorted array, find the minimum element in the array. Search must be must perform in O(log n) 

Algorithm: 
We know that if start index, mid index and end index elements are in increasing order, the start index has the minimum element in the array. We perform a binary search on our array and look for the condition to be true. If condition is not True, we compare value at start index to value at middle index. If value at start index is <= value at mid index, the smallest element exists on the right side of the middle element, else smallest element lies to the left. 

Solution: 
Debug code below with a few examples to understand it well. 
Here are a couple of tips to remember what operators to use. 
1. In statement 
    if nums[si] <= nums[mid] <= nums[ei] 
    we must use <= and not < because if we were testing an array of size 1, si = mid = ei and that means < operator would fail.
2. In two statements 
    if nums[si] <= nums[mid]:
        si = mid + 1
    remember, if we were testing an array of size 2, si = mid = 0 so we need to use <= operator not < operator. In the second statement si must be set to mid + 1 since for an array of size 2, si = mid = 0, and we si = 1 for next iteration

Time Complexity: O(log n) 
Space Complexity: O(1)
"""
print(__doc__)

class SolutionFindMin(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """        
        if not nums:
            return 0 
        
        # Init start and end index
        si, ei = 0, len(nums) - 1
        
        while si <= ei:
            mid = (si + ei) // 2   
            # if values at start, mid and end are sorted start index value is minimum break and return  
            # Why do we use <= instead of just <? Because eventually 
            # we might be checking a sub-array of size 1 or 2 at which point 
            # 2 or more indexes are equal.      
            if nums[si] <= nums[mid] <= nums[ei]:
                break 

            # Go to the right side of the array if left side is sorted.
            # Remember: use <= and not < because when comparing an array of 
            # size 2 si = mid = 0  
            if nums[si] <= nums[mid]:
                # Tip for remembering operator: 
                # for array of 2, first iteration yields si = mid = 0 
                # next iteration must move si to mid + 1
                si = mid + 1
            # Otherwise go to the left. 
            else:
                ei = mid
                

        return nums[si]

if __name__ == '__main__':
    s = SolutionFindMin()
    array = [3, 4, 5, 1, 2]
    print("Input: Array = {}".format(array))
    print("Answer: Minimum Element = {}".format(s.findMin(array)))
    print()    
    array = [5, 1 ,2 ,3, 4]
    print("Input: Array = {}".format(array))
    print("Answer: Minimum Element = {}".format(s.findMin(array)))
    
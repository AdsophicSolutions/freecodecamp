"""
Problem: 
Given a sorted array pivoted at some point search for a target value. Return index of target value and -1 if target does not exist. Search must be performed in O(log n) 

Algorithm: 
Let's start with an example array [4, 5, 1, 2, 3] pivoted at index 2 (value = 1). We are searching for target value of 5. If we consider the whole array where si = 0 and ei = length(array) - 1 = 4 our array mid point is index = 2. If value at start index <= value at mid point, we know that left side of the array is sorted, otherwise we know right side of array is sorted. In our example,  we compare array[0] (value = 4) to array[2] (value = 1). We now know left side of array is not sorted which means right side of array must be. Now we can check if our target value lies this right side sorted array. That means checking if array[2] <= target <= array[4] translating to (1 <= 5 <= 3). This condition is false, so we know target value can possibly only exist on left side of the array. Move ei = mid - 1 and continue the search 

Solution: 
Please debug a few examples of solution to understand algorithm. Tips to remember - in statement if nums[si] <= nums[mid]: remember to use <= and not < because if we were searching in an array of size 2 si and mid are both equal to 0.  

Time Complexity: O(log n) 
Space Complexity: O(1) 
"""
print(__doc__)

class SolutionArraySearch(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int                 
        """
        if not nums: 
            return -1
        
        if len(nums) == 1: 
            return 0 if nums[0] == target else -1
        
        si = 0 
        ei = len(nums) - 1
        location = -1
        while si <= ei: 
            mid = (si + ei) // 2    
            
            if nums[mid] == target: 
                location = mid
                break 
            
            # Left side of the array is sorted since nums[si] <= nums[mid]
            if nums[si] <= nums[mid]:
                # Since left side is sorted we can check for value on the left side 
                if nums[si] <= target <= nums[mid]:
                    ei = mid - 1
                # Value must exist on the right side. 
                else:
                    si = mid + 1
            # Right side is sorted
            else:
                # Check if value lies between mid and end. 
                if nums[mid] <= target <= nums[ei]:
                    si = mid + 1
                # Move search to left side 
                else:
                    ei = mid - 1
        
        return location
            

if __name__ == '__main__':
    s = SolutionArraySearch()
    array = [4, 5, 1, 2, 3]
    target = 2
    print("Input: Array = {}, Target = {}".format(array, target))
    print("Answer: Target Index = {}".format(s.search(array, target)))
    print() 
    
    array = [5, 1, 2, 3, 4]
    target = 2
    print("Input: Array = {}, Target = {}".format(array, target))
    print("Answer: Target Index = {}".format(s.search(array, target)))
    print() 
    
    array = [5, 1, 2, 3, 4]
    target = 9
    print("Input: Array = {}, Target = {}".format(array, target))
    print("Answer: Target Index = {}".format(s.search(array, target)))
    
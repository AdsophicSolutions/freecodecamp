class SolutionArraySearch(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        Performed in O(Log n) efficiency         
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
                if nums[si] <= target and nums[mid] >= target:
                    ei = mid - 1
                # Value must exist on the right side. 
                else:
                    si = mid + 1
            # Right side is sorted
            else:
                # Check if value lies between mid and end. 
                if nums[mid] <= target and nums[ei] >= target:
                    si = mid + 1
                # Move search to left side 
                else:
                    ei = mid - 1
        
        return location
            
            

if __name__ == '__main__':
    s = SolutionArraySearch()
    print(s.search([4, 5, 1, 2, 3], 2))
    print(s.search([5, 1, 2, 3, 2], 2))
    print(s.search([5, 1, 2, 3, 2], 9))
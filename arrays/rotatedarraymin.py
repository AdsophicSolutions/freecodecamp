class SolutionFindMin(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """        
        if not nums:
            return 0 
        
        si = 0 
        ei = len(nums) - 1
        while si < ei: 
            # if nums[si] is less than nums[ei]. This portion is sorted and 
            # so return value at si as the smallest value 
            if nums[si] < nums[ei]:
                break  
            
            # if si + 1 == ei and value at ei is lower, value at ei must be the first 
            # element in the rotated array and hence the smallest value 
            if si + 1 == ei and nums[si] > nums[ei]:
                si += 1
                break
            
            # find mid    
            mid = (si + ei) // 2
            
            # If value at si is less than value at mid 
            # since we've already established array isn't fully sorted (nums[si] > nums[ei])
            # we now mid is to the left of pivot point. hence si = mid 
            # if value at mid is higher, mid is to right of pivot point. 
            # make ei = mid 
            if nums[si] < nums[mid]: 
                si = mid
            else: 
                ei = mid
        
        return nums[si] 

if __name__ == '__main__':
    s = SolutionFindMin()
    print(s.findMin([3, 4, 5, 1, 2]))
    print(s.findMin([5, 1 ,2 ,3, 4]))
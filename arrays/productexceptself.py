class SolutionProductExceptSelf(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        Big O is O(n) for this algorithm 
        """
        if not nums or len(nums) == 1:
            return nums 
        
        output = [0] * len(nums)
        
        result = 1
        # Starting left side set value for each output element by multiplying previous element
        for i in range(len(nums)):
            output[i] = result 
            result *= nums[i]
        
        result = 1
        # Starting right side set value for each output element by multiplying previous element 
        for i in reversed(range(len(nums))):
            output[i] *= result 
            result *= nums[i]
        
        return output

if __name__ == '__main__':
    s = SolutionProductExceptSelf()
    print(s.productExceptSelf([2,3,1,4]))
    
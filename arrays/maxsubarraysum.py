class SolutionMaxSubArray(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0 
                
        max_sum = nums[0]
        cur_sum = nums[0]
        for i in range(1, len(nums)):
            # nums[i] + cur_sum is greater than num[i]
            # add nums[i] to running sum else
            # nums[i] becomes the new running sum 
            if nums[i] + cur_sum > nums[i]:
                cur_sum += nums[i]
            else:
                cur_sum = nums[i]
            
            # if running sum cur_sum > max_sum we have found
            # a new max_sum 
            if cur_sum > max_sum:
                max_sum = cur_sum
        
        return max_sum 
    
if __name__ == '__main__':
    s = SolutionMaxSubArray()
    print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
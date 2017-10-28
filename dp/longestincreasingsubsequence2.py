class SolutionLIS(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: 
            return 0
        
        if len(nums) == 1:
            return 1 
        
        is_descending = True
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                is_descending = False 
                break 

        if is_descending:
            return 1 

        is_ascending = True
        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]:
                is_ascending = False 
                break 

        if is_ascending:
            return len(nums)
    
        calc_matrix = [1]  * len(nums)        
        max_length = 1 
        
        for i in range(len(calc_matrix) - 1):        
            for j in range(i + 1, len(calc_matrix)):
                if nums[j] > nums[i]:
                    calc_matrix[j] = max(calc_matrix[i] + 1, calc_matrix[j])                 
                
                max_length = max(max_length, calc_matrix[j])
                    
        return max_length
    
    def getLIS(self, nums):
        if not nums: 
            return 0
        
        if len(nums) == 1:
            return 1 
        
        calc_matrix = [(1,[n]) for n in nums]         
        max_length = 1 
        max_sequence = [nums[0]]
        
        for i in range(len(calc_matrix) - 1):        
            for j in range(i + 1, len(calc_matrix)):
                if nums[j] > nums[i]:
                    if calc_matrix[j][0] < calc_matrix[i][0] + 1:                        
                        calc_matrix[j] = (calc_matrix[i][0] + 1, calc_matrix[i][1] + [nums[j]])
                    elif calc_matrix[j][0] == calc_matrix[i][0] + 1: 
                        if calc_matrix[j][1][0] > calc_matrix[i][1][0]:
                            calc_matrix[j] = (calc_matrix[j][0], calc_matrix[i][1][:] + [nums[j]])                
                
                if calc_matrix[j][0] > max_length: 
                    max_length = calc_matrix[j][0]
                    max_sequence = calc_matrix[j][1]
                    
        return max_sequence
            
if __name__ == '__main__':
    nums = [10, 9, 2, 8, 3, 7, 101, 105]
    s = SolutionLIS()
#     print(s.lengthOfLIS(nums))
    print(s.getLIS(nums))
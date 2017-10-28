class SolutionJumpGame(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums or len(nums) == 1:
            return True 
        
        cr = False
        hr = nums[0]
        cur_index = 1
        while cur_index <= hr:
            if nums[cur_index] + cur_index > hr: 
                hr = nums[cur_index] + cur_index
            
            if hr >= len(nums) - 1:
                cr = True
                break
                
            cur_index += 1
        
        return cr
    
if __name__ == '__main__':
    s = SolutionJumpGame()
    print(s.canJump([2,3,1,1,4]))
    print(s.canJump([3,2,1,0,4]))
"""
Problem: 
We are given an array where each element indicates money in a house
House robber cannot rob house next to each other. Calculate maximum that can 
be robbed.
 
Algorithm: 
Similar to house robber problem when houses are laid in line. Difference 
in this case 
1. Find out maximum money excluding last house.
2. Find out maximum money excluding first house  
Max of the two is maximum money that can be robbed.   
"""
print(__doc__)

class SolutionHouseRobber(object):
    def rob(self, nums):
        # Take care of corner cases        
        if not nums:
            return 0 
        if len(nums) == 1:
            return nums[0]
        
        # Init storage to calculate
        calc_money = [0] * len(nums)
        # Init first two spots
        calc_money[0] = nums[0]
        calc_money[1] = nums[1]
        
        # Iterate through rest of storage
        for i in range(2, len(calc_money)):
            # Another corner case.
            if i == 2:
                calc_money[i] = calc_money[i - 2] + nums[i]
            else: 
                # for all other houses maximum money 
                # that can be robbed is money in current 
                # house plus max of robbing one house over (i - 2) 
                # or two houses over (i - 3) 
                calc_money[i] = nums[i] + max(
                    calc_money[i - 2], 
                    calc_money[i - 3])
        
        # Maximum is the max between last and next to last house
        return max(calc_money[-1], calc_money[-2]) 

if __name__ == '__main__':
    print("Input:")
    nums = [20, 10, 30, 35, 20]
    print(nums)
    print("Answer:")
    s = SolutionHouseRobber()
    print(s.rob(nums))
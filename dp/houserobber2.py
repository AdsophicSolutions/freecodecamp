"""
Problem: 
We are given an array where each element indicates money in a house
House robber cannot rob house next to each other. Additionally, since houses 
are laid out in a circle, first house and last house are next to each other. 
Calculate maximum that can be robbed.
 
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
        if len(nums) == 2:
            return max(nums[0], nums[1])
        
        # Init storage to calculate. 
        # First calculate max money that can be robbed
        # excluding the last house
        # NOTE: calc_money array is one size smaller than 
        # nums
        calc_money = [0] * (len(nums) - 1) 
        # Init with money from first and second house. 
        calc_money[0] = nums[0]
        calc_money[1] = nums[1]
        
        # We go length of calc_money, this will exclude 
        # last house 
        for i in range(2, len(calc_money)):
            if i == 2:
                calc_money[i] = calc_money[i - 2] + nums[i]
            else: 
                calc_money[i] = nums[i] + max(
                    calc_money[i - 2],
                    calc_money[i - 3]
                    )
        
        # max money to be made excluding the last 
        max_money = max(calc_money[-1], calc_money[-2])
        
        # Reset calc_money. Again note size is 1 element 
        # smaller nums size 
        calc_money = [0] * (len(nums) - 1)
        # Init with money from second and third house 
        calc_money[0] = nums[1]
        calc_money[1] = nums[2]
        
        # We go length of calc_money which is one less 
        # than nums size 
        for i in range(2, len(calc_money)):
            # IMPORTANT: Use i + 1 to index nums array. 
            # We are dropping the first house 
            if i == 2:
                calc_money[i] = calc_money[i - 2] + nums[i + 1]
            else: 
                calc_money[i] = nums[i + 1] + max(
                    calc_money[i - 2],
                    calc_money[i - 3]
                    )
        
        # Max is equal to max money robbed excluding last house 
        # max money robbed excluding first house 
        return max(max_money, 
                   calc_money[-1], 
                   calc_money[-2])
        
if __name__ == '__main__':
    print("Input:")
    nums = [2,2,4,3,2,5]
    print(nums)
    s = SolutionHouseRobber()
    print("Answer:")
    print(s.rob(nums))
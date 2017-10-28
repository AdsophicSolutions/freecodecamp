"""
Problems: 
Given an array return the max sub-array product. Array can have both positive and negative numbers

Algorithm:
Trick here is to maintain a largest running negative and running positive and update max_product whenever max_product exceeds previously calculated max_product. 

Solution: 
To start set max_product, running_positive_running_negative to first element in array. Now for rest of the array update running_positive as max between current number, current number * running_positive and current_number and * running_negative. Similarly, running_negative is min between current_number, current_number * running_positive and current_number * running_negative. If running_positive exceeds max_product update it.  

Time Complexity: O(n) 
Space Complexity: O (1) 
"""
print(__doc__)

import itertools

class SolutionSubArrayProduct(object):
    def maxProduct(self, nums):
        max_product = running_positive = running_negative = nums[0]
        # Use itertools.islice instead of nums[1:] since it creates a 
        # new array 
        for num in itertools.islice(nums, 1, None):
            # update running_positive and running_negative
            running_positive, running_negative = (
                max(num, num * running_positive, num * running_negative ),
                min(num, num * running_positive, num * running_negative ))
            
            # update max_product if running_positive is greater 
            max_product = max(max_product, running_positive)
        
        return max_product

if __name__ == '__main__':
    s = SolutionSubArrayProduct()
    array = [2, -3, 3, 1, 2]
    print("Input= {}".format(array))
    print("Answer= {}".format(s.maxProduct(array)))
    print()
    array = [-3, 5, -4]
    print("Input= {}".format(array))
    print("Answer= {}".format(s.maxProduct(array)))

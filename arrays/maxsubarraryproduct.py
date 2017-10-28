class SolutionSubArrayProduct(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """        
        running_positive = None if nums[0] < 0 else nums[0]
        running_negative = 0 if nums[0] > 0 else nums[0]
        max_product = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i] == 0:
                running_positive = 0 
                running_negative = 0
            # if nums[i] > 0 multiply running_positive by this current number 
            # Multiply running negative only if current value is less than 0 
            elif nums[i] > 0:
                running_positive = nums[i] if not running_positive else running_positive * nums[i]    
                if running_negative < 0:
                    running_negative = running_negative * nums[i]
            else: 
                # current number is < 0. 
                # save running positive value
                temp = running_positive
                running_positive = running_negative * nums[i] 
                running_negative = nums[i] if not temp else temp * nums[i]
                
            if running_positive is not None and running_positive > max_product: 
                max_product = running_positive
            
        return max_product
    
    def maxProduct1(self, nums):
        max_product = running_positive = running_negative = nums[0]
        for num in nums[1:]:
            running_positive, running_negative = (
                max(num, num * running_positive, num * running_negative ),
                min(num, num * running_positive, num * running_negative ))
            
            max_product = max(max_product, running_positive)
        
        return max_product

if __name__ == '__main__':
    s = SolutionSubArrayProduct()
    print(s.maxProduct([2, -3, 3, 2]))
    print(s.maxProduct1([2, -3, 3, 2]))
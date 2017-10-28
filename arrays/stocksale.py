"""
Problem: 
Given a series of end of day stock prices, calculate maximum profit made by buying and selling stock once. Return 0 if no profit is possible 

Algorithm: 
Iterate through price list and track two values
min_so_far - Minimum value encountered so far. 
max_profit - Maximum profit so far. 
Maximum profit on a particular day is given by price that day 
minus minimum value before that day. If maximum profit on a day exceeds overall max profit make it new max profit

NOTE: If prices decline or stay same through price list there is no possibility of profit 

Time Complexity: O(n)
Space Complexity: O(1)
""" 
print(__doc__)

class SolutionMaxProfit(object):
    """
    Best time to buy and sell a stock
    """
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices or len(prices) <= 1:
            return 0
        
        # Set current min value to first element
        min_so_far = prices[0]
        # Max profit is initialized to 0
        max_profit = 0 
        
        for i in range(1, len(prices)):
            # If difference between price at i and cur_min_value is greater than max profit 
            # update max profit
            if prices[i] - min_so_far > max_profit: 
                max_profit = prices[i] - min_so_far
            
            # if current price is lower than previous cur_min_price 
            # make that the cur_min_price
            if prices[i] < min_so_far:
                min_so_far = prices[i]
        
        return max_profit
    
if __name__ == '__main__':
    s = SolutionMaxProfit()
    array = [7, 1, 5, 3, 6, 4]
    print("Input: {}".format(array))
    print("Answer: {}".format(s.maxProfit(array)))
    
"""
Problem:
Given a set of vertical lines of various heights that represent the walls of a rectangular return the maximum water that can be contained. 

Algorithm: 
Key to solving this problem is understanding the problem right. Look at the example below 
          |      
      5   |     | 4
          |     |
          |     |
  1 |     |     |       | 1
-----------------------------
    0     1      2       3

What we have above is four vertical lines of height 1, 5, 4, and 1. The maximum water that can be contained is between lines of height 5 and 4, since we can hold 4 * 1 amount of water between those two lines. On the other hand any other combination of lines can only hold 3 or less amount of water. For example, between line at index 0 of height 1 and line at index 3 of height 1 we can hold (3 - 0) * 1 of water. Similarly, amount of water between line at 2 (height 4) and line a 0 (height 1) is two. Meaning the amount of water than can be held between two lines is equal to distance between the two lines multiplied by height of the shorter line. 

Solution: 
Armed with this knowledge we can solve this problem. We start by picking the two lines at the end and work our way in. At every step we calculate the amount of water that can be held between those two lines (distance * min(line1, line2)). Update maximum if that value is greater than previous maximum. Next we decrement right side index if left line is taller and increment left side index otherwise. We continue doing this until indexes are equal  

Time Complexity: O(n) 
Space Complexity: O(1)  

VARIATION: Also return indexes, height of those two lines 
"""

print(__doc__)

class SolutionWaterContainer(object):
    def maxArea(self, height):        
        """
        :type height: List[int]
        :rtype: int
        """
        # Intialize starting points, max_water 
        i, j, max_water = 0, len(height) - 1, 0
        
        # Loop till i and j are not equal 
        while i < j:
            # distance between two lines 
            width = j - i 
            # update max_water if current water amount exceeds previously 
            # calculated max_water 
            max_water = max(max_water, width * min(height[i], height[j]))
            
            # Decrement right side index if left line is taller 
            if height[i] > height[j]:
                j -= 1
            # Increment left side index otherwise 
            else:
                i += 1
        
        # return result 
        return max_water

if __name__ == '__main__':
    print("Input:")
    lines = [1, 2, 5, 3, 2, 8, 9]
    print("Lines: {}".format(lines))
    s = SolutionWaterContainer()
    print("Answer: Max Water = {}".format(s.maxArea(lines))) 
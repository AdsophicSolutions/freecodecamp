class SolutionWaterContainer(object):
    def maxArea(self, height):        
        """
        :type height: List[int]
        :rtype: int
        """
        i, j, max_water = 0, len(height) - 1, 0
        while i < j: 
            width = j - i 
            max_water = max(max_water, width * min(height[i], height[j]))
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
        return max_water

if __name__ == '__main__':
    s = SolutionWaterContainer()
    print(s.maxArea([1, 2, 5, 3, 2, 8, 9]))
class SolutionTrappingWater(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """        
        total_water = 0
        max_left = 0 
        max_right = 0 
        si = 0 
        ei = len(height) - 1
        
        while si <= ei: 
            if height[si] < height[ei]:
                if height[si] > max_left:
                    max_left = height[si]
                else:
                    total_water += max_left - height[si]
                si += 1
            else:
                if height[ei] > max_right:
                    max_right = height[ei]
                else:
                    total_water += max_right - height[ei]
                ei -= 1                
        
        return total_water            
        

if __name__ == "__main__":
    s = SolutionTrappingWater()
#     print(s.trap([2,1,0,1,2]))
    print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
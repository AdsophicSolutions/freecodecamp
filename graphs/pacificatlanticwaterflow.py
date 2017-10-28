"""
Problem: 
Given an elevation map figure out cells can drain both into Pacific and Atlantic. Water can only move sideways or down 
(neighbors must have same or lower elevation) 
       P
    1,2,2,3,5
    3,2,3,4,4
  P 2,4,5,3,1 A
    6,7,1,4,5
    5,1,1,2,4
        A 

Solution: 
We separately process all cells that can drain into each ocean. Then we look for cells that are common. 
We perform a BFS of neighbors. For Pacific we know cells 1st row and 1st column can drain into water. 
In a queue we keep processing neighbors with cell values equal to or greater than current cell value. 
We make sure that same cells are not processed more than once. 
We repeat the process for last row and last column to figure out what cells drain into the Atlantic. 

Once we have both lists, return cells that exist in both. 
"""
print(__doc__)

class SolutionWaterFlow(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix: 
            return []
        
        def get_neighbors(m, n, size_m, size_n):
            neighbors = [
                (m - 1, n), 
                (m + 1, n),
                (m, n + 1),
                (m, n - 1)
            ]
            
            return [(m, n) for m, n in neighbors if m >= 0 and m < size_m and n >= 0 and n < size_n]
        
        # set to maintain list of cells that can flow into Pacific
        flow_into_pacific = set()
        flow_queue = []
        
        m = len(matrix)
        n = len(matrix[0])
        # add first column cells to queue 
        for i in range(m):
            flow_queue.append((i, 0))
        
        # add first row cells to queue 
        for i in range(1, n):
            flow_queue.append((0, i))
        
        # process queue
        while len(flow_queue) > 0: 
            cell = flow_queue.pop(0)
            flow_into_pacific.add(cell)
            
            # Process neighbors
            for neighbor in get_neighbors(cell[0], cell[1], m, n):
                # Queue any neighbor with equal or greater elevation and not already processed                
                if (matrix[cell[0]][cell[1]] <= matrix[neighbor[0]][neighbor[1]] and 
                    neighbor not in flow_into_pacific):
                    flow_into_pacific.add(cell)
                    flow_queue.append(neighbor)
        
        # set to maintain list of cells that can flow into Atlantic
        flow_into_atlantic = set()
        flow_queue = []
        
        # add last column cells to queue 
        for i in range(m):
            flow_queue.append((i, n - 1))
        
        # add last row cells to queue
        for i in range(n):
            flow_queue.append((m - 1, i))
        
        while len(flow_queue) > 0: 
            cell = flow_queue.pop(0)
            flow_into_atlantic.add(cell)
            
            # Process neighbors
            for neighbor in get_neighbors(cell[0], cell[1], m, n):
                # Queue any neighbor with equal or greater elevation and not already processed
                if (matrix[cell[0]][cell[1]] <= matrix[neighbor[0]][neighbor[1]] and 
                    neighbor not in flow_into_atlantic):
                    flow_into_atlantic.add(cell)
                    flow_queue.append(neighbor)
        
        return [[cell[0], cell[1]] for cell in flow_into_atlantic if cell in flow_into_pacific]
    
    
if __name__ == '__main__':
    s = SolutionWaterFlow()
    print("Answer:")
    print(s.pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]))    
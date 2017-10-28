"""
Problem: 
We are given a grid in form of a list of strings. String are made of '1's and '0's only. See below. 
["11110",
 "11010",
 "11000",
 "00000"]
 We want to return number of islands. '1' denotes land. Two pieces of land are connected 
 if they are neighbors. Neighboring pieces of land lie up, down, right or left of another piece. 
 Above example has a single island because all '1's are connected.  
 
Algorithm: 
Solution is to perform a BFS for all neighboring cells for each '1' we find and mark those cells as visited. 
We queue each neighboring cell not visited yet. Each '1' we find is a new island since BFS would have already 
marked all neighboring cells for the previous '1' 
"""
print(__doc__)

class SolutionNumberOfIslands(object):    
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0 
        
        def get_neighbors(m, n, size_m, size_n):
            neighbors = []
            if m - 1 >= 0:
                neighbors.append((m - 1, n))
            if m + 1 < size_m: 
                neighbors.append((m + 1, n))
            if n - 1 >= 0: 
                neighbors.append((m, n - 1))
            if n + 1 < size_n: 
                neighbors.append((m, n + 1))
            
            return neighbors
        
        number_of_islands = 0 
        
        m = len(grid)
        n = len(grid[0])
        # Init visited matrix 
        visited = [[False] * n for _ in range(m)]
        
        # iterate cells 
        for i in range(m):
            for j in range(n):
                # we found a not visited '1' 
                if grid[i][j] == '1' and not visited[i][j]:
                    # we found a new island  
                    number_of_islands += 1
                    # Add to queue
                    queue = [(i, j)]      
                    
                    # process till queue is empty
                    while len(queue) > 0: 
                        cell = queue.pop(0)
                        # mark cell as visited 
                        visited[cell[0]][cell[1]] = True
                        
                        # process neighbors
                        for neighbor in get_neighbors(cell[0], cell[1], m, n):
                            # Add to queue if neighbor is '1' and not yet visited 
                            if grid[neighbor[0]][neighbor[1]] == '1' and not visited[neighbor[0]][neighbor[1]]:
                                #THIS LINE IS VERY IMPORTANT. THIS PREVENTS THE SAME CELL FROM GETTING ADDED TO THE QUEUE
                                #AND REDUCES PROCESSING SIGNIFICANTLY. 
                                visited[neighbor[0]][neighbor[1]] = True
                                queue.append(neighbor)
                    
                    
        return number_of_islands 

if __name__ == '__main__':
    s = SolutionNumberOfIslands()
    print(s.numIslands(["11110",
                        "11010",
                        "11000",
                        "00000"]))
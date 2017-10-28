class SolutionUniquePaths(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m <= 0 or n <= 0: 
            return 0 
        
        matrix = [[1] * n for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                matrix[i][j] = matrix[i - 1][j] + matrix[i][j - 1]
        
        return matrix[-1][-1]
    
if __name__ == '__main__':
    s = SolutionUniquePaths()
    print(s.uniquePaths(10, 10))
'''
Created on Oct 19, 2017

@author: rahul
'''
def getWays(n, c):
    calc_matrix = [[0] * (n + 1) for _ in range(len(c) + 1)]
    for i in range(len(calc_matrix)):
        calc_matrix[i][0] = 1
        
    for i in range(1, len(calc_matrix)):
        for j in range(1, len(calc_matrix[0])):
            if j >= c[i - 1]: 
                calc_matrix[i][j] = (calc_matrix[i][j - c[i - 1]] + calc_matrix[i - 1][j])
            else: 
                calc_matrix[i][j] = calc_matrix[i - 1][j]
                
    return calc_matrix[-1][-1]

if __name__ == '__main__':
    n = 4
    c = [1, 2, 3]
    print(getWays(n, c))
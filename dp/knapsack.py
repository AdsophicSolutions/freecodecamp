def knapSack(W, wt, val):
    """
    Debug to understand the algorithm 
    O(xy) 
    """
    calc = [[0] * (W + 1) for _ in range(len(wt) + 1)]
    for i in range(len(calc)):
        for j in range(len(calc[0])):
            if i == 0 or j == 0:
                calc[i][j] = 0
            elif wt[i - 1] <= j:
                # current weight index only become relevant once value equals or exceeds weight value 
                # Take max weight value for current weight + previous row value at j - current weight and cell above                 
                calc[i][j] = max(val[i - 1] + calc[i - 1][j - wt[i - 1]], calc[i - 1][j])
            else:
                calc[i][j] = calc[i - 1][j]
    
    return calc[-1][-1]

if __name__ == '__main__':
#     val = [60, 100, 120]
#     wt = [10, 20, 30]
#     W = 50    
    val = [60, 200, 100]
    wt = [3, 2, 5]
    W = 9    
    print(knapSack(W, wt, val))
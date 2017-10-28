class SolutionCoingChange(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        calc = [[None] * (amount + 1) for _ in range(len(coins) + 1)]
        for i in range(len(calc)):
            calc[i][0] = 0 
            
        for i in range(1, len(calc)):
            for j in range(1, len(calc[0])):
                if j < coins[i - 1]: 
                    calc[i][j] = calc[i - 1][j]
                else: 
                    previousRow = calc[i - 1][j]
                    currentRow = calc[i][j - coins[i - 1]]  
                    if previousRow != None and currentRow != None:
                        calc[i][j] = min(currentRow + 1, previousRow)
                    elif previousRow != None and currentRow == None: 
                        calc[i][j] = previousRow 
                    elif previousRow == None and currentRow != None: 
                        calc[i][j] = currentRow + 1
                    else: 
                        calc[i][j] = None 
                        
        return -1 if calc[-1][-1] == None else calc[-1][-1]
    
    def coinChange1(self, coins, amount):
        calc = [None] * (amount + 1)
        calc[0] = (0, []) 
        
        for i in range(len(coins)):
            for j in range(coins[i], len(calc)):
                if calc[j - coins[i]] != None:
                    if calc[j] == None or calc[j][0] > calc[j - coins[i]][0] + 1: 
                        calc[j] = (calc[j - coins[i]][0] + 1, 
                            calc[j - coins[i]][1] + [coins[i]])  
                        
        return  -1 if calc[-1] == None else calc[-1]
        
if __name__ == '__main__':
    s = SolutionCoingChange()
#     print(s.coinChange([370,417,408,156,143,434,168,83,177,280,117], 9953))
    print(s.coinChange1([370,417,408,156,143,434,168,83,177,280,117], 9953))
#     print(s.coinChange1([1,2], 3))
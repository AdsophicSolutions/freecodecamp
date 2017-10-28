class SolutionLCS:
    def findLCS(self, str1, str2):
        calc_store = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]
        for i in range(1, len(calc_store)):
            for j in range(1, len(calc_store[0])):
                if str1[i - 1] == str2[j - 1]:
                    calc_store[i][j] = calc_store[i - 1][j - 1] + 1 
                else: 
                    calc_store[i][j] = max(
                        calc_store[i - 1][j], 
                        calc_store[i][j - 1] 
                        )                  
        
        return calc_store[-1][-1]
        

if __name__ == '__main__':
    s = SolutionLCS()
#     print(s.findLCS('axyzaabbc', 'axyzaakkbd'))
    print(s.findLCS('acbd', 'aacb'))
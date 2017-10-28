class SolutionIsInterleaving():
    def is_interleaving(self, a, b, c):
        if not a and not b and not c: 
            return True 
        
        if not c: return False 
        if not a: return b == c 
        if not b: return a == c 
        
        if len(a) + len(b) != len(c):
            return False 
        
        match = [[False] * (len(b) + 1) for _ in range(len(a) + 1)]
        match[0][0] = True 
        
        for i in range(1, len(match)):
            if a[i - 1] == c[i - 1]:
                match[i][0] = match[i - 1][0]
            else:
                match[i][0] = False
        
        for i in range(1, len(match[0])): 
            if b[i - 1] == c[i - 1]:
                match[0][i] = match[0][i - 1]
            else:
                match[0][i] = False
        
        for i in range(1, len(match)):
            for j in range(1, len(match[0])):
                if a[i - 1] == c[i + j - 1] and b[j - 1] != c[i + j - 1]:
                    match[i][j] = match[i - 1][j]
                elif b[j - 1] == c[i + j - 1] and a[i - 1] != c[i + j - 1]:
                    match[i][j] = match[i][j - 1]
                elif b[j - 1] == c[i + j - 1] and a[i - 1] == c[i + j - 1]:
                    match[i][j] = match[i][j - 1] or match[i - 1][j]
                else:
                    match[i][j] = False 
        
        return match[-1][-1] 

if __name__ == '__main__':
    s = SolutionIsInterleaving()
    print(s.is_interleaving("ab", "b", "abb"))
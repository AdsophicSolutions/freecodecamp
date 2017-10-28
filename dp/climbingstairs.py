def climbingStairs(steps, total):
    calc = [[0] * (total + 1) for _ in range(len(steps) + 1)]
    for i in range(len(calc)):
        calc[i][0] = 1 
        
    for i in range(1, len(calc)):
        for j in range(1, len(calc[0])):
            if j < steps[i - 1]:
                calc[i][j] = calc[i - 1][j]
            else: 
                calc[i][j] = calc[i][j - steps[i - 1]] + calc[i - 1][j]                   
    
    return calc[-1][-1]

def climbingStairs1(steps, total):
    calc = [0] * (total + 1)
    calc[0] = (1, []) 
    
    for i in range(1, total + 1):
        for j in range(len(steps)):
            if steps[j] <= i: 
                calc[i] += calc[i - steps[j]]
    
    return calc[-1]

if __name__ == '__main__':
    print(climbingStairs1([2, 3, 7], 10))
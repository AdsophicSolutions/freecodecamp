"""
Problem: 
Two problems with similar but slightly different solutions. 
One problem involves calculating number of ways to score a specified number of total points. Here is an example. In American football points are awarded from set of (2, 3, 6, 7, 8). We want to calculate in how many different ways we can get to score of say, 21. In this calculation order does not matter. To illustrate, a team can only score 5 points one way, scoring 2 and scoring 3 points. The order of the scores is irrelevant.
Second problem is similar, but in this case order matters. Consider this example. We are given total number of steps and a set of steps that can be taken in one go. We are asked to calculate number of ways we can get to the top step. In this problem  order is relevant. Meaning, if total number of steps = 3 and you were permitted to take 1 or 2 steps at a time, we could get to top step in three different ways (1, 1, 1), (1, 2) and (2, 1)    

Algorithm & Solution: 
A dynamic programming based solution suits this kind of problem best. We can sub-divide the overall problem into sub-problems and work our way to the final answer. In both these problems we sub-divide it into a problem to be solved for each step size for every possible score. To illustrate, for ways to score problem we consider the number of ways we can score 0 points using score of 2 (1 way, by considering we score 2 zero times). Next we consider how many ways we can score 1 point by way of a 2 score (0, since 1 is not a multiple of 2). But we can score 2 points one way using a 2 score. Once we complete this calculation for a 2 score we continue it for 3 score and so on.  

Time Complexity: O(n^2) 
Space Complexity: O(n) or O(n^2): Refer to individual solutions 
"""
print(__doc__)

class SolutionGetToEnd(object):
    def waysToScore(self, steps, total):
        """
        Scoring sequence is irrelevant 
        
        Time Complexity: O(n^2)
        Space Complexity: O(n^2)        
        :type steps: List
        :type total: int
        :rtype: int        
        """
        # Create our memoization matrix 
        # rows will represent the different scores
        # columns represent score
        # Since we want to include 0 as a possible finals score number of columns = total + 1
        # To avoid a custom statement for row 0 we set number of rows = steps + 1 
        calc = [[0] * (total + 1) for _ in range(len(steps) + 1)]
        
        # First element of each row is set to 1, this is to signify 
        # that we can score 0 points 1 way 
        for i in range(len(calc)):
            calc[i][0] = 1 
        
        # Outer loop goes through each step/score available     
        for i in range(1, len(calc)):
            # Inner loop iterates to the end of the final score
            for j in range(1, len(calc[0])):
                # If j < current step size (steps[i - 1] - remember i = 1 is calculating for step at index 0)  
                # it cannot contribute to final score 
                if j < steps[i - 1]:
                    calc[i][j] = calc[i - 1][j]
                # else total ways to get to j (current score) is 
                # number of ways we can get to score up to previous step 
                # size + value[calculating score - current step size]
                else: 
                    calc[i][j] = calc[i][j - steps[i - 1]] + calc[i - 1][j]                   
        
        return calc[-1][-1]

    def waysToScoreSpaceOptimized(self, steps, total):
        """
        Scoring sequence is irrelevant
        
        Time Complexity: O(n^2)
        Space Complexity: O(n)
        :type steps: List
        :type total: int
        :rtype: int
        """
        # To save space we create two rows to maintain running score
        # we switch current and previous after each iteration. 
        cur, prev = [0] * (total + 1), [0] * (total + 1)
        
        # First element of each row is set to 1, this is to signify 
        # that we can score 0 points 1 way 
        cur[0] = prev[0] = 1
        
        # Outer loop goes through each step/score available 
        for i in range(1, len(steps) + 1):
            # Inner loop iterates to the end of the final score
            for j in range(1, len(cur)):
                # If j < current step size (steps[i - 1] - remember i = 1 is calculating for step at index 0)  
                # it cannot contribute to final score 
                if j < steps[i - 1]:
                    cur[j] = prev[j]
                # else total ways to get to j (current score) is 
                # number of ways we can get to score up to previous step 
                # size + value[calculating score - current step size]
                else: 
                    cur[j] = cur[j -steps[i - 1]] + prev[j]
            # Switch references between prev and cur
            cur, prev = prev, cur 
        
        # Return prev not cur: statement cur, prev = prev, cur switches 
        # references in the last iteration. 
        return prev[-1]
    
    def climbingStairs(self, steps, total):
        """
        Sequence is relevant
        
        Time Complexity: O(n^2)
        Space Complexity: O(n)
        :type steps: List
        :type total: int
        :rtype: int
        """
        # Create our memoization array. size = total + 1 to include 
        # space for value 0  
        calc = [0] * (total + 1)
        
        # First element of each row is set to 1, this is to signify 
        # that we can get to step 0 1 way 
        calc[0] = 1 
        
        # Outer loop goes through end of total number of steps 
        # NOTE: Outer loop and inner loop ordering is reversed 
        # in this solution compared to other solutions in this module 
        for i in range(1, total + 1):
            # Inner loop iterates through each step size 
            for j in range(len(steps)):
                # Total ways to get to current step 
                # is previously calculated ways to current step + 
                # value[calculating score - current step size]
                if steps[j] <= i: 
                    calc[i] += calc[i - steps[j]]
                    
        return calc[-1]

if __name__ == '__main__':
    s = SolutionGetToEnd()
    
    # In ways to score order does not matter. 
    # Meaning getting to 9 by way of 2, 7 or by way of 7,2 is considered a single way. 
    steps = [2, 3, 6, 7, 8]
    total = 5 
    print("Input: possible scores = {}, total score = {}".format(steps, total))
    print("Answer: O(n^2) Space complexity = {}".format(s.waysToScore(steps, total)))
    print("Answer: O(n) Space complexity = {}".format(s.waysToScoreSpaceOptimized(steps, total)))    
    print()
    total = 21 
    print("Input: possible scores = {}, total score = {}".format(steps, total))
    print("Answer: O(n^2) Space complexity = {}".format(s.waysToScore(steps, total)))
    print("Answer: O(n) Space complexity = {}".format(s.waysToScoreSpaceOptimized(steps, total)))
    
    print() 
    steps = [1, 2]
    # In climbing stairs order matters. 
    # For example we can get to 3rd step if we were permitted to go 1 step 
    # at a time or 2 steps at a time in three ways (1, 2) (2, 1) or (1, 1, 1)
    total = 10 
    print("Input: step sizes = {}, total steps = {}".format(steps, total))
    print("Answer: {}. Space Complexity is always O(n)".format(s.climbingStairs(steps, total)))
    print() 
    total = 25 
    print("Input: step sizes = {}, total steps = {}".format(steps, total))
    print("Answer: {}. Space Complexity is always O(n)".format(s.climbingStairs(steps, total)))
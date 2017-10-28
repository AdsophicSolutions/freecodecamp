class SolutionCombinationsSum(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        calc = [0] * (target + 1)
        calc[0] = 1
        
        for i in range(1, target + 1):
            for n in nums:
                if i >= n:
                    calc[i] += calc[i - n]
        
        return calc[-1]

if __name__ == '__main__':
    s = SolutionCombinationsSum()
    print(s.combinationSum4([1,2,3], 4))
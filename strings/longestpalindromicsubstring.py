class SolutionLongestPalindrome(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return s 
        
        # Let us create calculation matrix
        memo = [[False] * len(s) for _ in range(len(s))]
        
        # All strings of size 1 are palindromes 
        for i in range(len(memo)):
            memo[i][i] = True 
        
        # Calculate if size 2 strings are palindromes
        start_index = 0
        end_index = 0
        max_length = 1
        for i in range(len(memo) - 1):
            if s[i] == s[i + 1]:
                memo[i][i + 1] = True 
                if max_length == 1:
                    start_index = i 
                    end_index = i + 1
                    max_length += 1
        
        # Calculate for rest of string sizes 
        for k in range(3, len(s) + 1):
            for i in range(len(s) - k + 1):
                # find end index for current string 
                j = i + k - 1                
                # if values match set True or False from 
                # enclosed string 
                if s[i] == s[j]:                    
                    memo[i][j] = memo[i + 1][j - 1]
                    # if cell value is true and current string 
                    # length is greater than previous length 
                    if memo[i][j] and k > max_length:
                        start_index, end_index, max_length = i, j, k
                # else we don't have a palindrome
                else: 
                    memo[i][j] = False 
        
        return s[start_index: end_index + 1]
    
if __name__ == '__main__':
    s = SolutionLongestPalindrome()
    print(s.longestPalindrome("yahoooohay"))
    print(s.longestPalindrome("2071702"))
    print(s.longestPalindrome("abcddc"))
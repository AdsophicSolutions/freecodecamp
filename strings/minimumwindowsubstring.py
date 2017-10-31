class SolutionMinWindow(object):
    def minWindow2(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s or not t or len(s) < len(t):
            return ""
        
        char_count = {}
        for c in t: 
            if c not in char_count:
                char_count[c] = 0 
            char_count[c] += 1
        
        start = 0 
        start_match, end_match = 0, 0
        min_length = len(s) + 1
        ncovered = 0
        
        for end in range(len(s)):
            if s[end] in char_count: 
                char_count[s[end]] -= 1
                if char_count[s[end]] >= 0:
                    ncovered += 1
            if ncovered == len(t):
                while start <= end:                    
                    if s[start] in char_count: 
                        char_count[s[start]] += 1
                        if end - start + 1 < min_length:
                            start_match = start
                            end_match = end + 1 
                            if start_match - end_match == len(t):
                                return s[start_match:end_match]
                            min_length = end_match - start_match                                                
                        if char_count[s[start]] == 1:
                            ncovered -= 1
                            start += 1
                            break                        
                    start += 1
        
        return "" if min_length == len(s) + 1 else s[start_match:end_match]
                
        
if __name__ == '__main__':
    s = SolutionMinWindow()
#     print(s.minWindow2("ADOBECODEBANC", "ABC"))
#     print(s.minWindow2("acbbaca", "aba"))
#     print(s.minWindow2("aaflslflsldkalskaaa", "aaa"))
    print(s.minWindow2("aa", "aa"))

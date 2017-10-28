class SolutionValidParanthesis(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        is_valid_comb = lambda c1, c2: c1 + c2 == ')(' or c1 + c2 == '][' or c1 + c2 == '}{'
        
        matcher = []
        close_match_set = set([')', '}', ']'])
        open_match_set = set(['(', '{', '['])
        
        for i in range(len(s)):        
            c = s[i]
            if not matcher and c in close_match_set:
                return False 
            
            if c in open_match_set:
                matcher.append(c)
            else: 
                if not is_valid_comb(c, matcher.pop()):
                    return False 
        
        return not matcher 

if __name__ == '__main__':
    s = SolutionValidParanthesis()
    print(s.isValid("[[[]]{}]"))
    print(s.isValid("{}[[)"))
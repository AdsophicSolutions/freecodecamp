class SolutionCountSubstrings:
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return 0 
        
        def grow_and_count(i):
            count = 1
            if i + 1 < len(s) and s[i] == s[i + 1]: 
                count = 2
                size = 1
                is_palindrome = True 
                while is_palindrome:
                    if i - size < 0 or i + 1 + size > len(s) - 1: break
                    if s[i - size] == s[i + 1 + size]:
                        count += 1
                    else:
                        is_palindrome = False 
                    size += 1
                
            size = 1
            is_palindrome = True 
            while is_palindrome:
                if i - size < 0 or i + size > len(s) - 1: break
                if s[i - size] == s[i + size]:
                    count += 1
                else:
                    is_palindrome = False 
                size += 1
                
            return count
        
        p_count = 0
        for i in range(len(s)):
            p_count += grow_and_count(i)
        
        return p_count 

if __name__ == '__main__':
    s = SolutionCountSubstrings();
    string = "abc"
    print(s.countSubstrings(string))
    string = "aaaa"
    print(s.countSubstrings(string))
    string = "aaaaabbcc"
    print(s.countSubstrings(string))
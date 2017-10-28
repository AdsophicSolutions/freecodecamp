class SolutionIsPalindrome(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        
        c_string = []
        for i in range(len(s)):
            c = s[i]
            if self.is_alphanumeric(c):
                c_string.append(c.lower())
        
        si = 0 
        ei = len(c_string) - 1
        
        while si < ei:                      
            if c_string[si] != c_string[ei]:
                return False
            si += 1
            ei -= 1
        
        return True
    
    def is_alphanumeric(self, c):
        return ((ord(c) >= ord('a') and ord(c) <= ord('z')) or
                (ord(c) >= ord('A') and ord(c) <= ord('Z')) or
                (ord(c) >= ord('0') and ord(c) <= ord('9')))

if __name__ == '__main__':
    s = SolutionIsPalindrome()
    print(s.isPalindrome("A man, a plan, a canal: Panama"))
    print(s.isPalindrome("race a car"))
    
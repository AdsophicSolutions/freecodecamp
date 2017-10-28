class SolutionUniqueSubstring(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: 
            return 0
        
        
        i, j = 0, 1 
        char_set = set()
        char_set.add(s[0])
        max_string = s[0]
        max_length = 1
        cur_string = s[0]
        cur_length = 1
        
        while j < len(s):
            if s[j] in char_set: 
                sub_size = 1
                while s[i] != s[j]:
                    char_set.remove(s[i])                                        
                    i += 1
                    sub_size += 1
                    cur_length -= 1
                    
                i += 1                    
                cur_string = cur_string[sub_size:] + s[j]
            else: 
                char_set.add(s[j])
                cur_string += s[j]
                cur_length += 1
                
            j += 1
            
            if len(cur_string) > len(max_string):
                max_string = cur_string 
            
            if cur_length > max_length: 
                max_length = cur_length
        
        return max_length
    
if __name__ == '__main__':
    s = SolutionUniqueSubstring()
    print(s.lengthOfLongestSubstring('abcabcbb'))
    print(s.lengthOfLongestSubstring('bbbbb'))
    print(s.lengthOfLongestSubstring('pwwkew'))
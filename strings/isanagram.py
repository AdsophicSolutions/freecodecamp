"""
Problem: 
Compare if two strings are anagrams or not 

Algorithm 1: 
Add each character from one string to a dictionary and maintain 
count for each character. 
Now for each character in the second string reduce count for character 
found in dictionary. If character cannot be found return false. 

Return true if count for each character from dictionary is equal to 0. 

Algorithm 2: 
Return results of a comparison between sorted versions of the two strings. 
"""
print(__doc__)

class SolutionAnagram(object):
    def isAnagram1(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """        
        if not s and not t:
            return True
        if bool(s) != bool(t):
            return False 
        
        char_dictionary = {}
        for c in s: 
            if c in char_dictionary: 
                char_dictionary[c] += 1 
            else:
                char_dictionary[c] = 1 
        
        for c in t:
            if c in char_dictionary: 
                char_dictionary[c] -= 1
            else:
                return False 
        
        return not any(cv for cv in char_dictionary.values() if cv != 0)
    
    def isAnagram2(self,s, t):
        # Take care of corner cases 
        if not s and not t:
            return True
        if bool(s) != bool(t):
            return False 
        
        # return result of sorted comparison of the strings 
        return sorted(s) == sorted(t)
    
if __name__ == '__main__':
    s = SolutionAnagram()
    tests = [
        ["anagram","nagaram"],
        ["rat","car"]
        ]
    
    for t in tests:
        print("Input:")
        print(t[0] + ',' + t[1])
        print("Answer: Algo 1")
        print(s.isAnagram1(t[0], t[1]))        
        print("Answer: Algo 2")
        print(s.isAnagram2(t[0], t[1]))
        print()
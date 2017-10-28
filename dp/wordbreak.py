"""
Problem: 
Given a non-empty string s and a dictionary wordDict, determine if s can be broken down into a series of 
words from dictionary

Example
s = "abcdef",
dict = ["abc", "def"].
Answer: True "abcdef" is "abc" + "def" 

Algorithm: 
Declare a storage of size len(s) + 1 initialized to False. Set first location to True. 
Value at each subsequent location = storage location value at [location - wordLength] 
if a word is equal to s from location - wordlength to current location. 

Last index of storage is final result    
"""
print(__doc__)

class SolutionWordBreak(object):    
    def wordBreak(self, s, wordDict):
        # Create results storage
        calc_store = [False] * (len(s) + 1)
        # Set index 0 to True 
        calc_store[0] = True 
        
        # declare is_equal method to speed up string compare 
        def is_equal(str1, start_index, str2):
            for i in range(len(str2)):
                if str1[start_index + i] != str2[i]:
                    return False 
            
            return True 
        
        # for each index in calc_store    
        for i in range(1, len(calc_store)):            
            for word in wordDict:
                word_length = len(word) 
                # if word matches s from i - word_length. 
                # value at i = value at i - word_length
                if i - word_length >= 0 and is_equal(s, i - word_length, word): 
                    calc_store[i] = calc_store[i - word_length]
                    # If value at i is now True 
                    # we can skip rest of the dictionary 
                    if calc_store[i]:  
                        break 
        
        # last index of calc_store is the final result 
        return calc_store[-1]
    

if __name__ == '__main__':
    
    sol = SolutionWordBreak()
    s = "aaaaaaaaaaaaaaaaaaaaacdeaaaaaab"
    wordDict = ["a", "ab", "cde"]
    print("Input:")
    print("s = {0}, dictionary = {1}".format(s, wordDict))
    print("Answer") 
    print(sol.wordBreak(s, wordDict))
    
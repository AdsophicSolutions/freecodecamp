"""
Problem: 
Given a list of strings, return list of list where 
each list is a group of strings that are anagrams 

Algorithm: 
In a dictionary use sorted version of each input string as key   
to group strings into anagrams. Return values from output
"""
print(__doc__)

class SolutionGroupAnagrams(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        output = {}
        for s in strs:          
            # get sorted value for string  
            s_value = ''.join(sorted(s))
            
            # Add sorted value to output 
            # with current string. 
            if s_value not in output: 
                output[s_value] = [ s ]
            else:
                output[s_value].append(s)
        
        # return values from output 
        return [li for li in output.values()]

if __name__ == '__main__':
    str_list = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print("Input:")
    print(str_list)
    print("Answer:")
    s = SolutionGroupAnagrams()
    print(s.groupAnagrams(str_list))
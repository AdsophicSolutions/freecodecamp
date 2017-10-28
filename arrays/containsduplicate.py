'''
Problem: 
Return true if an array of nums contains a duplicate value

Algorithm: 
Store numbers encountered so far. If we encounter same number again return True. If no duplicate is found, return False 

Solution: 
Iterate through numbers array checking if each number is stored in dup dictonary, return True if we find it, else add number to the dictionary  

Time Complexity: O(n)
Space Complexity: O(n)
'''
print(__doc__)

class SolutionContainsDuplicate(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False
        # declare set to check for duplicates         
        dup = set() 
        
        for n in nums:
            # if dup already contains value return True
            if n in dup:
                return True
            # Add number to hash set
            dup.add(n)
        
        # No duplicates found. Return False
        return False

if __name__ == '__main__':
    s = SolutionContainsDuplicate()
    
    array = [2,3,4,7,2]
    print("Input: {0}".format(array))    
    print("Answer: {}".format(s.containsDuplicate(array)))
    print() 
    array = [2,3,4,7,8]
    print("Input: {0}".format(array))    
    print("Answer: {0}".format(s.containsDuplicate(array)))
    
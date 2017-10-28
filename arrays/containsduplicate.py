'''
Return true if an array of nums contains a duplicate value 
'''
class SolutionContainsDuplicate(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False         
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
    print(s.containsDuplicate([2,3,4,7,2]))
    print(s.containsDuplicate([2,3,4,7,8]))
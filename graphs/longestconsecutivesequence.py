"""
Problem
Given a list of unique numbers find out the longest consecutive series of numbers. 
For example in [129, 3, 2, 783, 4, 23, 24, 5] longest consecutive series of numbers is 2, 3, 4, 5. Hence 
answer should be 4. Algorithm must complete in O(n) time complexity. 

NOT INTUITIVE: Revise often 

Algorithm: 
Store each number in a dictionary with value of False. Value is used to indicate if 
number is previously processed. Take first number from list (as part of an iteration). 
Add this number to process queue. Dequeue number, mark as processed. Now look for 
number + 1 and number - 1 in dictionary. If they exist and haven't been processed already add to 
queue. Count sequence size as you process numbers. if seq size is greater than previous max 
when queue is empty update max. Continue to next number in list. Only process number if 
not previous processed. 
"""

print(__doc__)

class SolutionLongestConsecutive(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # add all numbers to a hash table with value false 
        storage = {} 
        for n in nums:
            storage[n] = False
                
        max_length = 0
        for n in nums:
            # if this number is unprocessed 
            if not storage[n]:                
                queue = []
                # Add number to queue
                queue.append(n)
                
                seq = 0
                while len(queue) > 0:
                    v = queue.pop(0)
                    storage[v] = True
                    seq += 1 
                    # if next number exists but unprocessed add to queue
                    if v + 1 in storage and not storage[v + 1]:
                        queue.append(v + 1)
                    # if previous number exists but unprocessed add to queue
                    if v - 1 in storage and not storage[v - 1]:
                        queue.append(v - 1)
                
                max_length = max(max_length, seq)
        
        return max_length
    
if __name__ == '__main__':
    s = SolutionLongestConsecutive()
    print(s.longestConsecutive([100, 4, 200, 1, 3, 2]))
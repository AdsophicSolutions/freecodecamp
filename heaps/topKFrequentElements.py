"""
Problem: 
Get top most frequently occurring elements from a list of numbers. 

Algorithm: 
Demonstrate use of min-heap. 
1. Create a dictionary with frequency counts. 
2. Add items to min_heap list. 
3. Heapify min_heap. 
4. Get nLargest k numbers from list. 

NOTE: You must use min-heap not max-heap. Max-heap would not work in cases 
where we wanted to maintain only list of top x element in descending order 
size. In a max-heap largest number is popped out first.  

Time Complexity: 
O(n) + O(log(k) * n)
"""
import heapq

print(__doc__)

class SolutionTopKFrequent(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        frequency = {}
        for n in nums: 
            if n in frequency: 
                frequency[n] += 1
            else: 
                frequency[n] = 1
        
        min_heap = [(v, key) for (key, v) in frequency.items()]
        heapq.heapify(min_heap)
                
        return [p[1] for p in heapq.nlargest(k, min_heap)]
            

if __name__ == '__main__':
    print("Answer:")    
    nums = [1,1,1,3,3,2,2,3]
    print("Input list:{}".format(nums))
    k = 2
    s = SolutionTopKFrequent()
    print("Result:{0}".format(s.topKFrequent(nums, k)))
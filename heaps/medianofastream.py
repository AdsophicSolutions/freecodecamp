"""
Problem:
Continuous median. Maintain a median as new numbers are received via a stream 

Solution: 
Use a min-heap and a max-heap. min-heap is a structure where min value always resides on top 
max-heap is a structure where max value always resides on top. As we receive a new value we pushpop 
value from min heap (Min heap maintains the right side of numbers). Min heap pops out min value 
which we add to max heap. If max heap size is now greater than min heap we move largest element from 
max heap (this maintains left side of numbers stream) back to min-heap. 
Median is average of element 0 of both heaps if heaps are equal size or first element of min-heap (odd number 
of total numbers)  
"""
import heapq

print(__doc__)

class ContinuousMedian(object):
    def __init__(self):
        self._min_heap = []
        self._max_heap = []
    
    def add_element(self, number):
        # push-pop new number from min_help. Add popped number to 
        # max-heap 
        heapq.heappush(self._max_heap, 
                       -heapq.heappushpop(self._min_heap, number))
        
        # if length of max-heap is larger pop top value to min-heap 
        if len(self._max_heap) > len(self._min_heap):
            heapq.heappush(self._min_heap, 
                       -heapq.heappop(self._max_heap))
            
    
    def get_median(self):
        if not self._min_heap or not self._max_heap: 
            return 0 
        
        # median is average of top elements where heaps are equal size 
        # othewise median is top element of min-heap 
        return (0.5 * (self._min_heap[0] + -self._max_heap[0]) 
                if len(self._min_heap) == len(self._max_heap)
                else self._min_heap[0]) 
        
if __name__ == '__main__':
    print("Answer:")
    array = [1, 0, 3, 5, 2, 0, 1, 5, 1, 2, 3, 8, 3, 1]
    c = ContinuousMedian()    
    for a in array: 
        print("Adding:{}".format(a))
        c.add_element(a)
        print("Median:{}".format(c.get_median()))
        
"""
Problem: 
Merge a list of sorted linked lists. 

Algorithm: 
Demonstrate use of min-heap to sort multiple linked lists. 
We iterate through each linked list and add values to min_heap  
Next we heapify the min_heap. This is O(n) time complexity. 
Now we can create our new linked list by extracting one min element at a time 
Time complexity of the operation is O(n log n) bringing total time complexity to 
O(n) + O(n log n)
"""
import heapq

print(__doc__)

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class SolutionMergeKLists(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """        
        min_heap = []    
        # Add elements from all linked lists to min_heap 
        while any(l for l in lists if l != None):
            for i, l in enumerate(lists):
                if l: 
                    min_heap.append(l.val)
                    lists[i] = l.next

        if not min_heap:
            return None
        
        # Now heapify 
        heapq.heapify(min_heap)
        
        prev = None
        head = None  
        # Create new linked list by popping top element from heap 
        while min_heap:
            node = ListNode(heapq.heappop(min_heap))
            if not head:
                head = node 
            if prev:
                prev.next = node 
            prev = node
        
        return head
    
def print_list(head):
    output = []
    while head: 
        output.append(str(head.val))
        head = head.next 
    
    print("List: [ " + " , ".join(output) + " ]")
        
if __name__ == '__main__':
    l = []
    # Create List 1 
    prev = None 
    head = None 
    for i in range(0, 10, 2):     
        node = ListNode(i)
        if not head: 
            head = node
        if prev: 
            prev.next = node 
        prev = node 
        
    print_list(head)
    l.append(head)
    
    # Create List 2 
    prev = None 
    head = None 
    for i in range(1, 10, 2):     
        node = ListNode(i)
        if not head: 
            head = node
        if prev: 
            prev.next = node 
        prev = node
        
    print_list(head)    
    l.append(head)
    
    # Merge and print 
    s = SolutionMergeKLists()
    print_list(s.mergeKLists(l))
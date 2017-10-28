"""
Problem: 
Return True if a singly linked list has a cycle 

Algorithm: 
Accomplished using two pointers to traverse link list. 
One pointer traverse a single node, second one traverses 
two at a time. If at any point first pointer and second 
pointer point to the same node we have a cycle. If faster
pointer reaches end of list no cycle exists. 
"""
print(__doc__)

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class SolutionHasCycle(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head: 
            return False 
        
        slower = head
        faster = head.next 
        while faster: 
            if slower == faster: 
                return True 
            slower = slower.next
            if faster.next:
                faster = faster.next.next
            else: 
                break
                
        return False 

def print_list(head, length):
    display = []
    
    while length:
        display.append("[{0}]".format(head.val))
        head = head.next
        length -= 1
        
    print("->".join(display))
    
if __name__ == '__main__':
    # Test 1 
    prev = None
    head = None 
    length = 0
    for i in range(1, 9):
        node = ListNode(i)
        if not head:
            head = node
        if prev: 
            prev.next = node        
        prev = node
        length += 1
    print("Input:")      
    print_list(head, length)    
    s = SolutionHasCycle()
    print("Answer:")    
    print(s.hasCycle(head))
    print() 
    
    # Test 2 
    print("Input:") 
    prev.next = head.next.next
    print_list(head, length + 1)
    print("Answer:")    
    print(s.hasCycle(head))
    
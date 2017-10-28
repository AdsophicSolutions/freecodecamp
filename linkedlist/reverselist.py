"""
Problem: 
Given first node of a link list reverse list 

Algorithm: 
Important to remember solution cannot be executed using 
2 pointers. 3 are required. Algorithm best understood through 
code comments 
"""
print(__doc__)

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class SolutionRerveseList(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # head is None return
        if not head:
            return head 
        
        # set prev to head
        prev = head
        # set cur to prev.next 
        cur = prev.next
        # prev.next becomes None since it 
        # is the last node after list is reversed
        prev.next = None
        
        # while cur pointer is not None: 
        # Make a not of how this will work if list is a single node. 
        # loop never gets executed. 
        while cur:
            # Save cur.next in forward
            forward = cur.next
            # step reverses direction
            cur.next = prev
            # move prev to cur 
            prev = cur
            # move cur to saved pointer
            cur = forward
            
        # prev is new head pointer 
        return prev
    
def print_list(head):
    display = []
    
    while head:
        display.append("[{0}]".format(head.val))
        head = head.next
        
    print("->".join(display))
    
if __name__ == '__main__':    
    prev = None
    head = None 
    for i in range(1, 9):
        node = ListNode(i)
        if not head:
            head = node
        if prev: 
            prev.next = node        
        prev = node
    print("Original List:")      
    print_list(head)
    s = SolutionRerveseList()
    print("Reversed List:")    
    print_list(s.reverseList(head))
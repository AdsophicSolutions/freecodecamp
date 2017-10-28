from freecodecamp.trees.treeserializer import TreeSerializer

class SolutionSameTree(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """                
        # both are None return True
        if not p and not q:
            return True 
        # One is None and the other is not, return False 
        if bool(p) != bool(q):
            return False
        
        def compare(t1_node, t2_node):
            # if both sides are None return True
            if not t1_node and not t2_node:
                return True 
            
            # If only one side is None return False
            if bool(t1_node) != bool(t2_node):
                return False 
            
            # Both nodes are not None. return False if values not equal
            if t1_node.val != t2_node.val:
                return False
            
            # return comparison between left side and right side
            return compare(t1_node.left, t2_node.left) and compare(t1_node.right, t2_node.right)
        
        # Call compare
        return compare(p, q)
            

if __name__ == '__main__':
    ser = TreeSerializer()
    # Example 1 
    tree1_string = "1,2,3,4"    
    tree1 = ser.deserialize(tree1_string)
    
    tree2_string = "1,2,3,4"
    tree2 = ser.deserialize(tree2_string)
    
    s = SolutionSameTree()
    print("Example 1")
    print("Tree 1: " + tree1_string)
    print("Tree 2: " + tree2_string)
    print("Trees equal: {0}".format(s.isSameTree(tree1, tree2)))
    print()
    
    # Example 2
    tree1_string = "1,2,n,4"    
    tree1 = ser.deserialize(tree1_string)
    
    tree2_string = "1,2,3,n"
    tree2 = ser.deserialize(tree2_string)
    
    s = SolutionSameTree()
    print("Example 2")
    print("Tree 1: " + tree1_string)
    print("Tree 2: " + tree2_string)
    print("Trees equal: {0}".format(s.isSameTree(tree1, tree2)))
    
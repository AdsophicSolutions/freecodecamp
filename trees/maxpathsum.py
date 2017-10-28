from freecodecamp.trees.treeserializer import TreeSerializer

class SolutionMaxPathSum(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # if root is None return 0 
        if not root:
            return 0 
        
        # define function to calculate max 
        def find_max(node, previous_sum):
            node_plus_children = (previous_sum +
                                  (0 if not node.left else node.left.val) + 
                                  (0 if not node.right else node.right.val)
                                 )
            left_max = node_plus_children
            if node.left:
                left_max = max(left_max, node.left.val)
                left_max = find_max(node.left, left_max)
            
            right_max = node_plus_children
            if node.right: 
                right_max = max(right_max, node.right.val)
                right_max = find_max(node.right, right_max)
            
            return max(previous_sum, left_max, right_max)
        
        return find_max(root, root.val)

if __name__ == '__main__':
    ser = TreeSerializer()    
    root = ser.deserialize("1,2,3")
    s = SolutionMaxPathSum()
    print(s.maxPathSum(root))
from freecodecamp.trees.treeserializer import TreeSerializer

class SolutionInvertTree(object):
    def invertTree(self, root):
        """
        :type root: freecodecamp.trees.treenode.TreeNode
        :rtype: freecodecamp.trees.treenode.TreeNode
        """
        # if root is None return
        if not root:
            return root
        
        # recursive function invert
        def invert(node):
            # swap left and right nodes
            node.left, node.right = node.right, node.left
            # if left is not None call recursively
            if node.left:
                invert(node.left)
            # if right is not None calle recursively
            if node.right:
                invert(node.right)
        
        # calls invert function
        invert(root)
        # return root. tree inverted in-place
        return root
    
if __name__ == '__main__':
    ser = TreeSerializer()    
    root = ser.deserialize("1,2,3,4,5,6,7")
    print("Original:")
    ser.print_hierarchy(root)
    s = SolutionInvertTree()
    s.invertTree(root)
    print()
    print("Inverted:")
    ser.print_hierarchy(root)
#     print(ser.serialize(root))
    
"""
Problem:
Find Lowest Common Ancestor for a BST(Binary Search Tree)

Solution:
Though the below implementation uses recursion, it is not required, 
because each traversal takes out left or right section of the tree  

"""

class SolutionLCA(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def traverse_and_find(node, p, q):            
            if node.val < p.val and node.val < q.val:
                return traverse_and_find(node.right, p, q)
            
            if node.val > p.val and node.val > q.val:
                return traverse_and_find(node.left, p, q)
            
            return node
        
        return traverse_and_find(root, p, q)
if __name__ == '__main__':
    pass
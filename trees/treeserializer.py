from freecodecamp.trees.treenode import TreeNode 

class TreeSerializer:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return '';
        
        output = [str(root.val)]
        bfs = [root]
        
        while len(bfs) > 0: 
            node = bfs.pop(0)
            if node.left or node.right: 
                if node.left: 
                    bfs.append(node.left)
                output.append("n" if not node.left else str(node.left.val))
                if node.right:
                    bfs.append(node.right)
                output.append("n" if not node.right else str(node.right.val))
            else: 
                output.append("n")
                output.append("n")
        
        first_non_null = -1 
        while output[first_non_null] == 'n':
            first_non_null -= 1        
        return ",".join(output) if first_non_null == -1 else ",".join(output[:first_non_null + 1])
    
    def print_hierarchy(self, root):
        bfs = [root]
        while len(bfs) > 0:
            node = bfs.pop(0)
            print(
                "Tree value: {0}{1}{2}".format
                (
                    node.val, 
                    "" if not node.left else " Left value:" + str(node.left.val),
                    "" if not node.right else " Right value:" + str(node.right.val)
                )
                )
            if node.left:
                bfs.append(node.left)
            if node.right:
                bfs.append(node.right)
                 
                
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data: 
            return None 
        
        datavals = data.split(',')        
        head = TreeNode(int(datavals[0]))
        child_index = 1
        bfs = [head]
        
        while len(bfs) > 0: 
            node = bfs.pop(0)
            if child_index >= len(datavals):
                break 
            if datavals[child_index] != "n": 
                left_child = TreeNode(int(datavals[child_index]))
                node.left = left_child
                bfs.append(left_child)
            
            if child_index + 1 >= len(datavals):
                break
            
            if datavals[child_index + 1] != "n": 
                right_child = TreeNode(int(datavals[child_index + 1]))
                node.right = right_child
                bfs.append(right_child)
            
            child_index += 2
        
        return head
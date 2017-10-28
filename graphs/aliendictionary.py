class SolutionAlienOrder(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        def is_heirarchy_valid(parent_char, cur_char):
            parent_node = node_dictionary[parent_char]
            while parent_node != head:
                if parent_node.val == cur_char:
                    return False
                parent_node = parent_node.parent 
                 
            return True
        
        def in_heirarchy(parent_char, cur_char):
            parent_node = node_dictionary[cur_char].parent
            while parent_node != head:
                if parent_node.val == parent_char:
                    return True
                parent_node = parent_node.parent 
                 
            return False
            
        node_dictionary = {}
        head = TrieNode(None)
        
        for c in words[0]:
            if c not in node_dictionary: 
                node = TrieNode(c)
                node_dictionary[c] = node
                head.children[c] = node 
                node.parent = head
        
        for i in range(1, len(words)):  
            compare_completed = False 
                      
            for j in range(len(words[i])):
                c_prev = None if j >= len(words[i - 1]) else words[i - 1][j]
                c_cur = words[i][j]
                
                if not c_prev or compare_completed:
                    if c_cur not in node_dictionary:
                        node = TrieNode(c_cur)
                        node_dictionary[c_cur] = node
                        head.children[c_cur] = node
                        node.parent = head
                        
                    continue
                
                if c_prev == c_cur:
                    continue
                
                compare_completed = True 
                
                if c_cur in node_dictionary:
                    if not is_heirarchy_valid(c_prev, c_cur):
                        return ''
                    if not in_heirarchy(c_prev, c_cur):
                        node = node_dictionary[c_cur]
                        del node.parent.children[c_cur]
                        node_dictionary[c_prev].children[c_cur] = node
                        node.parent = node_dictionary[c_prev]
                else: 
                    node = TrieNode(c_cur)
                    parent_node = node_dictionary[c_prev] 
                    parent_node.children[c_cur] = node
                    node.parent = parent_node
                    node_dictionary[c_cur] = node
        
        result = []
        queue = [ head ]
        while len(queue) > 0:
            node = queue.pop(0)
            if node.val: result.append(node.val)
            
            for child in node.children.values():
                queue.append(child)
        
        return ''.join(result)

class TrieNode(object):
    def __init__(self, val):
        self.val = val
        self.children = {}
        self.parent = None 

if __name__ == '__main__':
#     words =  [
#           "wrt",
#           "wrf",
#           "er",
#           "ett",
#           "rftt"
#         ]
#     words =  [
#           "z",
#           "x",
#           "z"
#         ]

#     words = ["ri","xz","qxf","jhsguaw","dztqrbwbm","dhdqfb","jdv","fcgfsilnb","ooby"]
    words = ["a","b","ca","cc"]
    
    s = SolutionAlienOrder()
    print(s.alienOrder(words))
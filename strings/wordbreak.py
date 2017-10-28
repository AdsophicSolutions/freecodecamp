class TrieNode:
    def __init__(self, val):
        self.val = val
        self.children = {}
        self.num_of_children = 0 
        self.word = None 

class Trie:
    def __init__(self):
        self._head = TrieNode("*")
    
    def add_node(self, word):
        cur_node = self._head
        cur_node.num_of_children += 1        
        for c in word:
            if c not in cur_node.children:
                node = TrieNode(c)
                cur_node.children[c] = node
            else: 
                node = cur_node.children[c]
            
            node.num_of_children += 1
            cur_node = node 
        
        cur_node.word = word 
        
    
    def traverse(self, c, start_node = None):
        start_node = self._head if not start_node else start_node
        if c in start_node.children: 
            return start_node.children[c]
        else:
            return None
    
    def is_word(self, node):
        return bool(node.word)  

class SolutionWordBreak(object):
    def __init__(self):
        self._trie = Trie()
        
    def wordBreak(self, s, wordDict): 
        if not wordDict: 
            return False
               
        wordDict.sort()
        self._trie.add_node(wordDict[0])
        
        for word in wordDict[1:]:
            if not self.is_word_broken(word):
                self._trie.add_node(word)
        
        return self.is_word_broken(s)
    
    def is_word_broken(self, s):
        queue = []
        queue.append(s)    
        
        is_found = False
        while len(queue) > 0:
            qs = queue.pop(0)
            cur_node = None
            for i, c in enumerate(qs):
                cur_node = self._trie.traverse(c, start_node = cur_node)
                if cur_node:
                    if self._trie.is_word(cur_node):
                        if not qs[i + 1:]:
                            is_found = True 
                            break
                        else: 
                            queue.append(qs[i + 1:])
                else:
                    break
                
            if is_found:
                break
        
        return is_found
    
if __name__ == '__main__':
    s = SolutionWordBreak()
    wordDict = ["leet", "code"]
    inp_str = "leetcode"
    print(s.wordBreak(inp_str, wordDict))
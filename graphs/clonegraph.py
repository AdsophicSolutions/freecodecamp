# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class SolutionCloneGraph:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node: 
            return None 
        
        clone_head = None
        cloned_nodes = {}
        processed_nodes = set() 
        
        node_queue = []
        node_queue.append(node)
        
        while len(node_queue) > 0: 
            n = node_queue.pop(0)
            
            if n.label in cloned_nodes: 
                clone = cloned_nodes[n.label]
            else: 
                clone = UndirectedGraphNode(n.label)
                cloned_nodes[n.label] = clone
            
            if not clone_head:
                clone_head = clone
            
            for neighbor in n.neighbors: 
                if neighbor.label in cloned_nodes: 
                    n_clone = cloned_nodes[neighbor.label]
                else: 
                    n_clone = UndirectedGraphNode(neighbor.label)
                    cloned_nodes[neighbor.label] = n_clone
                
                clone.neighbors.append(n_clone)
                
                if neighbor.label != n.label and n_clone.label not in processed_nodes:                                        
                    node_queue.append(neighbor)
                
                processed_nodes.add(clone.label)
        
        return clone_head 
         
def create_graph(graph_string):
    graphs = {}
    first = None
    
    for graph_info in graph_string.split('#'):
        rel_list = []
        graph_info.split(',')
        for con_info in graph_info.split(','):
            rel_list.append(con_info)
            if con_info not in graphs:
                g = UndirectedGraphNode(con_info)
                graphs[con_info] = g
            else: 
                g = graphs[con_info]
                
            if not first: 
                first = g
        
        g = graphs[rel_list[0]]
        for i in range(1, len(rel_list)):
            g.neighbors.append(graphs[rel_list[i]])
            graphs[rel_list[i]].append(g)       
               
    
if __name__ == '__main__':
    input = "0,1,5#1,2,5#2,3#3,4,4#4,5,5#5"
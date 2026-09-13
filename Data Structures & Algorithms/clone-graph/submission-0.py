"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        cloned_map = {}

        def dfs(node):
            if node is None:
                return None

            if node in cloned_map:
                return cloned_map[node]
                
            new_node = Node(node.val, None)
            cloned_map[node] = new_node
            
            for nbr in node.neighbors:
                node_new = dfs(nbr)
                new_node.neighbors.append(node_new)
            
            return new_node 

        return dfs(node)

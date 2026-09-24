"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # deep copy of graph
        # dfs approach 
        # use a hashmap to map the node to its clone 
        # visit different nodes, create new nodes (store on hashmap)
        # if the node has been visited we stop cloning 

        if not node:
            return None

        clone_map = {}

        def dfs(curr_node):
            
            if curr_node  in clone_map:
                return clone_map[curr_node]

            
            new_node = Node(curr_node.val , [])
            clone_map[curr_node] = new_node

            for neighbor in curr_node.neighbors:
                new_node.neighbors.append(dfs(neighbor))

            return new_node 


        return dfs(node)

        


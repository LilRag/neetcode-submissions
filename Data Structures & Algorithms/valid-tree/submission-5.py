class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # valid tree must not have any cycles and a tree with n nodes must have n-1 edges
        from collections import deque
        from collections import defaultdict 
        
        if len(edges) != n-1:
            return False

        visited = set([0])
        adj_list = defaultdict(list)

        for u,v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        queue = deque([0])

        while queue:
            curr = queue.popleft()
            for adj_node in adj_list[curr]:
                if adj_node not in visited:
                    visited.add(adj_node)
                    queue.append(adj_node)

        
        if len(visited) == n and len(edges) == n-1 :
            return True

        else:
            return False
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
       # tree of n nodes , 0 to n-1 , array of n-1 edges 
       # we can create trees out of any node as our root node 
       # for each node as the root, we have to traverse and find its height
       # then we have to keep track of all the trees with min height
       # a hashmap that stores for each root the height? 
       # taking each node as root we do like dfs traversal and find the height and store it in the hashmap? 

        from collections import deque
        from collections import defaultdict

        adj_list = defaultdict(list)

        if n == 1:
            return [0]

        indegree = [0]*n
        for u,v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
            indegree[v] += 1
            indegree[u] += 1  

        queue = deque()

        for index, i in enumerate(indegree):
            if i == 1:
                queue.append(index)

        remaining_nodes = n 
        while remaining_nodes > 2:
            leaves_count = len(queue)
            remaining_nodes -= leaves_count 
            for _ in range(leaves_count):
                node = queue.popleft()
                for nbr in adj_list[node]:
                    indegree[nbr] -= 1 
                    if indegree[nbr] == 1:
                        queue.append(nbr)

            
        return list(queue) 
    
                

        

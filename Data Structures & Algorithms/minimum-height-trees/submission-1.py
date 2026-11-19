class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        from collections import deque 
        from collections import defaultdict

        adj_list = defaultdict(list)
        degree = [0]*n

        if n <= 2 :
            return [i for i in range(n)]

        for x,y in edges:
            adj_list[x].append(y)
            adj_list[y].append(x)

        for i in range(n):
            degree[i] = len(adj_list[i])

    
        queue = deque()

        for i in range(n):
            if degree[i] == 1:
                queue.append(i)


        remaining_nodes = n 
        while remaining_nodes > 2: 
            layer_size = len(queue)
            remaining_nodes -= layer_size

            for _ in range(layer_size):
                leaf = queue.popleft()
                for neighbour in adj_list[leaf]:
                    degree[neighbour] -=1

                    if degree[neighbour] == 1:
                        queue.append(neighbour)
        

        return list(queue)

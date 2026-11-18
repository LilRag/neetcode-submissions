class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        # buid reverse adjacency list 
        # track outdegrees
        # push the outdegree = 0 nodes onto the list
        # run bfs 
        # return sorted list 

        from collections import defaultdict, deque

        n = len(graph)

        rev_graph = defaultdict(list)
        out_degree = [0]*n

        for u in range(n):
            out_degree[u] =  len(graph[u])
            for v in graph[u]:
                # original edge: u -> v 
                # reverse edge: v - > u 
                rev_graph[v].append(u)

        queue = deque()
        output = []

        for i in range(n):
            if out_degree[i] == 0:
                queue.append(i)

        while queue:
            curr = queue.popleft()
            output.append(curr)

            for neighbour in rev_graph[curr]:
                out_degree[neighbour] -= 1
                if out_degree[neighbour] == 0:
                    queue.append(neighbour)
        
        return sorted(output)
                
        
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # given a set of known division rations between pairs of variables (like a/b = 2.0) and b/c = 3.0
        # we need to calculate division ratios between new pairs 
        # a/b * b/c = a/c = 6
        # b/a = 1/2
        # a = 1 

        # we can model variables and equations as a graph 
        # nodes each unique variable string 
        # "a" , "b" , "c"   
        # directed efges , A/B = k 
        # a -> b with weight k , b->a with weight 1/k
        from collections import defaultdict, deque 

        graph = defaultdict(list)
        # building the weighted graph 
        for (a,b), val in zip(equations, values):
            graph[a].append((b,val))
            graph[b].append((a, 1.0/val))


        def bfs(start: str, end: str) ->float:
            
            if start not in graph or end not in graph:
                return -1.0

            # edge case , dividing a valid variable by itself 
            if start == end:
                return 1.0

            queue = deque([(start,1.0)])
            visited = {start}

            while queue:
                curr_node, curr_prod = queue.popleft()

                if curr_node == end:
                    return curr_prod

                for neighbour, weight in graph[curr_node]:
                    if neighbour not in visited:
                        visited.add(neighbour)
                        queue.append((neighbour, curr_prod*weight))

            # edge case 3 , variable exists but are disconnected
            return -1.0
        
        return [bfs(c,d) for c,d in queries ] 

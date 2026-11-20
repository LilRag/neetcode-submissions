class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # network of n directed nodes
        # 1 to n 
        # times(ui, vi, ti)
        # ui is the source node
        # vi is the target node
        # ti is the time it takes for a signal to travel from source to the target node 
        # k represents the node that we will send a signal from
        # time it takes for all n nodes to recieve the signal, if impossible return -1 

        # build the directed adjaceny list 
        # initialize distancess as inf 
        # min heap stores tuples of (time_so_far, node)
        # run dijkstras algorithm
        # explore outgoing neighbors 
        
        from collections import defaultdict 
        import heapq
        
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v,w))

        dist = [float('inf')]*(n+1)
        dist[k] = 0 

        # time_so_far, node 
        min_heap = [(0,k)]

        while min_heap:
            curr_time, u = heapq.heappop(min_heap)

            # skip stale enteries where we already found a faster route to u 
            if curr_time > dist[u]:
                continue

            for v, travel_time in graph[u]:
                new_time = curr_time + travel_time 
                if new_time < dist[v]:
                    dist[v] = new_time
                    heapq.heappush(min_heap, (new_time, v))

        max_time = max(dist[1:])
        return max_time if max_time != float('inf') else -1


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # n airports from 0 to n-1 
        # airports are connected by flights 
        # flights[i] = [from_i, to_i, price_i]
        # from_i to to_i with cost 
        # no duplicate flights and an airport to itself 
        # src, dst and k (maximum number of stops we can make from src to dest)
        # return -1 

        import heapq 
        from collections import defaultdict

        adj = defaultdict(list)
        for u,v, price in flights:
            adj[u].append((v, price))

        min_stops = [float('inf')]*n

        #min heap storing (total_cost, current_airport, stops used)
        min_heap = [(0, src, 0)]

        while min_heap: 
            cost, u, stops = heapq.heappop(min_heap)

            # since we pop by lowest cost, the first time we pop dst is guaranteed optimal 
            if u == dst:
                return cost 

            # skuip if we ve exceedeed the allowed stopsm, or if we ve already reached 
            if stops > k or stops >= min_stops[u]:
                continue 

            min_stops[u] = stops

            for v, price in adj[u]:
                heapq.heappush(min_heap, (cost + price , v , stops + 1))

        return -1  

        
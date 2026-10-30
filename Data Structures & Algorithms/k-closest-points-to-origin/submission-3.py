class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import heapq
        import math 


        max_heap = []
        res = []

        for x, y in points:
            distance = math.sqrt(x**2 + y**2)
            heapq.heappush(max_heap, [-distance, x, y])

        while len(max_heap) > k:
            heapq.heappop(max_heap)

        for i in max_heap:
            res.append([i[1], i[2]])

        return res
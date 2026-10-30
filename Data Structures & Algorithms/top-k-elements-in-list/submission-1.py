class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq
        
        counts = dict(Counter(nums))
        
        min_heap = []
        res = []

        for key, value in counts.items():
            heapq.heappush(min_heap, [value, key])

        while len(min_heap) > k:
            heapq.heappop(min_heap)


        for i in min_heap:
            res.append(i[1])
        
        return res
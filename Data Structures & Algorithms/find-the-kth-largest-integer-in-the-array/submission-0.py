class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        #kth largest 
        # we set a min heap of only k values
        import heapq 
        min_heap = []
        nums_array = [int(x) for x in nums if x.isdigit()]

        for i in nums_array:
            heapq.heappush(min_heap, i)

        while len(min_heap) > k:
            heapq.heappop(min_heap)

        return str(min_heap[0])
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # min heap of k elements
        # kth largest is always the root then 
        import heapq

        min_heap = []

        for i in range(len(nums)):
            heapq.heappush(min_heap, nums[i])

            if len(min_heap) > k:
                heapq.heappop(min_heap)

        return heapq.heappop(min_heap)

                
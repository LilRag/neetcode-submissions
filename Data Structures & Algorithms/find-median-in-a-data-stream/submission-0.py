

class MedianFinder:
    import heapq
    def __init__(self):
        # max_heap stores the smaller half (values negated for max-heap behavior)
        self.small = []  
        # min_heap stores the larger half
        self.large = []  

    def addNum(self, num: int) -> None:
        # Step 1: Add to small (max-heap)
        heapq.heappush(self.small, -num)
        
        # Step 2: Ensure small's largest <= large's smallest
        val = -heapq.heappop(self.small)
        heapq.heappush(self.large, val)
        
        # Step 3: Maintain size balance: len(small) >= len(large)
        if len(self.large) > len(self.small):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return float(-self.small[0])
        return (-self.small[0] + self.large[0]) / 2.0
        
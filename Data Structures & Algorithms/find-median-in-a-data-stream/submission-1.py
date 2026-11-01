class MedianFinder:

    def __init__(self):
        self.small = [] #small half , using max heap 
        self.large = [] # large half, using min heap 

        # max of small half and min of large half , give us the middle elements

    def addNum(self, num: int) -> None:
        # add it to the max heap 
        heapq.heappush(self.small, -num)
        
        #ensure the max of smallest <= min of largest 
        val = -heapq.heappop(self.small)
        heapq.heappush(self.large, val)

        # if more elements in large , rebalance it 
        if len(self.large) > len(self.small):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)
        

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return float(-self.small[0])

        else:
            return (-self.small[0] + self.large[0])/2
        
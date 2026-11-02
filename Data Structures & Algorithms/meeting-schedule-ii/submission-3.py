"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    import heapq

    def minMeetingRooms(self, intervals: list[list[int]]) -> int:
        if not intervals:
            return 0

        # Step 1: Sort by start time
        intervals.sort(key=lambda x: x.start)

        # Step 2: Min-heap stores end times of active rooms
        min_heap = []

        for interval in intervals:
            # If the earliest ending meeting finished before or when this one starts, reuse room
            if min_heap and min_heap[0] <= interval.start:
                heapq.heappop(min_heap)

            # Allocate room (either the reused room with a new end time, or a brand new room)
            heapq.heappush(min_heap, interval.end)

        return len(min_heap)
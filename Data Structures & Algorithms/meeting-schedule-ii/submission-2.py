"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
# min heap , for room that frees us earliest , we can prolly compare the end time to the current interval start time , if end time lesser than we can popit out of the list and updare the new end time 

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0 
        intervals.sort(key = lambda x: x.start)

        free_rooms = []

        heapq.heappush(free_rooms, intervals[0].end)


        for i in range(1, len(intervals)):
            # if the room that frees up earlies is free before this meeting start
            # we can reuse the room , pop it from the heap 
            if free_rooms[0] <= intervals[i].start:
                heapq.heappop(free_rooms)
            
            heapq.heappush(free_rooms, intervals[i].end)
 

        
        return len(free_rooms) 
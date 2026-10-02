class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # integer capacity (empty seats)
        # trips -> num passengers, from , to 
        # return true if possible to pick up and drop off all passengers for all trips 
        # 4 , 1 , 2 -> passenger = 4 , pick up from 1 and drop to 2 
        # 3 , 2 , 4 -> only after the first trip completes , we can do this trip as there is no capacity during the first trip , but because its from 2 to 4 it works out 

        # global location of car , global capacity 
        # we equate it to the location of the first trip 
        # then we keep the remainder capacity as the global capacity 
        # we finish the trip and update location and capacity 
        # but if there is a trip that is in between the existing trip , we check if theres enough capacity , if not we can directly return false
        # if possible , we still have to keep track of ongoing trips 
        # so we use min heap for this? we can store the distance and passesngers 
        # pop that out and update the global location and free up the capacity 

        # sort the trips by start location 
        import heapq

        trips.sort(key = lambda x:x[1])
        min_heap = []
        current_passengers = 0 

        for num_passengers, start, end in trips:
            while min_heap and min_heap[0][0] <= start:
                _, dropped_passengers = heapq.heappop(min_heap)
                current_passengers -= dropped_passengers

            current_passengers += num_passengers 
            if current_passengers > capacity:
                return False

            heapq.heappush(min_heap, (end, num_passengers ))

        return True  
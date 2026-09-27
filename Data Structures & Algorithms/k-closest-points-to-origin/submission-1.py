class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # 2d array points, points[i] -> coordinates [xi,yi]
        # integer k 
        # find the k closest points to origin
        # euclidian distance from origin 

        # max heap, farther away nodes , occupy root positions of the heap  
        # so do we store the coordinate, and distance ? 
        # sort the node based on the distance ?
        # and then return top k 
        # instead we can keep only k elements in the heap and return the heap at the end of the loop 
        # new element which is lesser than max , max gets thrown out to accomodate new element

        import heapq
        max_heap =[]
        for x, y in points:
            # for max heap , we store it by negating the values, we are able to store max as root 
            distance = -(x**2 + y**2)
            heapq.heappush(max_heap, (distance, [x,y]))

            if len(max_heap) > k:
                heapq.heappop(max_heap)
        result = []
        for dist,coords in max_heap:
            result.append(coords)

        return result
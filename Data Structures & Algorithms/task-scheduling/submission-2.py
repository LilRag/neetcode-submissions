class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # process most frequent tasks
        # max heap (-frequency, task, processing time)
        # use queue that acts as a cool down buffer (remaining_count, available_time) 
        import heapq
        from collections import deque

        counts = Counter(tasks)
        

        max_heap =[-cnt for cnt in counts.values()]
        heapq.heapify(max_heap)

        queue = deque() # remaining_count, available_time 
        time = 0 

        while max_heap or queue:
            time += 1 
            
            if max_heap:
                count = 1 + heapq.heappop(max_heap)

                if count < 0:
                    queue.append((count, time + n))
            
            if queue and queue[0][1] == time:
                ready_cnt, _ = queue.popleft()
                heapq.heappush(max_heap, ready_cnt)

        return time 



        
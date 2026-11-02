class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # global time
        # create a min heap , with processing time , original index 
        # when cpu idle, we pop from min heap , add the processing time to global time
        # if processes enque time occur, we append that to the min heap 
        
        
        # sort tasks first 
        import heapq

        sorted_tasks = sorted([(task[0], task[1], i) for i, task in enumerate(tasks)])
        min_heap = []

        time = 0 
        res = []
        i = 0 
        n = len(tasks)

        while i < n or min_heap:
            if not min_heap and time < sorted_tasks[i][0]:
                time = sorted_tasks[i][0]

            while i < n and sorted_tasks[i][0] <=time:
                heapq.heappush(min_heap, (sorted_tasks[i][1], sorted_tasks[i][2]))
                i += 1 

            proc_time, original_idx = heapq.heappop(min_heap)
            time += proc_time 
            res.append(original_idx)

        return res 

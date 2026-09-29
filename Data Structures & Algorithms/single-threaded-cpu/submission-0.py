class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # n tasks, 0 to n-1 
        # tasks[i] = [enquetime, processigtime]
        # single threaded cpu, that can process at most one task at a time 
        # cpu is idle, when no available tasks to process
        # if cpu is idle , cpu chooses one with the shortest processing time, if multiple short tasks, smallest id is picked
        # once a task is started to process, cpu will process the entire task without stopping 
        
        # so we need to keep track of a global time 
        # at idle cpu, we have to see which task is available 
        # if none, increment the time and check again 
        # once we choose a task , we can directly skip that many time steps ahead (processing time )
        # now with our new time , we check all the available tasks and pick the smallest 
        # we can store this in a min heap of processing time ?


        import heapq 
        # index, enquetime and processingtime 
        tasks_with_id = [[task[0], task[1], index] for index, task in enumerate(tasks)]
        # sort by enqueu time 
        tasks_with_id.sort(key = lambda x: x[0])

        result =[]
        available_tasks = [] # min heap storing tuples (processing time , original index)
        global_time = 0
        task_idx = 0
        n = len(tasks)

        while len(result) < n:
            # if idle we jump to arrival time 
            if not available_tasks and global_time < tasks_with_id[task_idx][0]:
                global_time = tasks_with_id[task_idx][0]
            # enqueue all tasks that arrived at or before current time             
            while task_idx < n and tasks_with_id[task_idx][0] <= global_time:
                heapq.heappush(
                    available_tasks,
                    (tasks_with_id[task_idx][1], tasks_with_id[task_idx][2]),
                )
                task_idx += 1 

            # process a task
            proc_time, original_id = heapq.heappop(available_tasks)
            global_time +=  proc_time 
            result.append(original_id)

        return result 
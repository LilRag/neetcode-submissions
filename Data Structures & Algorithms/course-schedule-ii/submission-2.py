class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # prerequisites array; prerequisites[i] = [a,b] should take course b before a 
        # total num courses you are required to take 
        # true if its possible to finish the courses 
        # false if not 

        # topological sort 
        # build the adjacency list with prereq as the key and courses as value
        # indegree list , where index signifies the course and value is the indegree connections
        # maintain a queue, when the indegree becomes 0 , add it to the queue , increment a completed count 

        from collections import defaultdict
        from collections import deque 

        adj_list = defaultdict(list)
        in_degree =[0]*numCourses
        order_list = []
        completed = 0

        for course, prereq in prerequisites:
            adj_list[prereq].append(course)
            in_degree[course] += 1 

        queue = deque()
        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)


        while queue:
            course_idx = queue.popleft()
            order_list.append(course_idx)
            completed += 1 

            for neighbor in adj_list[course_idx]:
                in_degree[neighbor] -= 1 
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
    
        if completed == numCourses:
            return order_list

        else:
            return []


        

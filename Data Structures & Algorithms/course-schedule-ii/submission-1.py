class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        from collections import deque
        sorted_order =[]

        indegree =[0]*numCourses
        adj_list ={i:[] for i in range(numCourses)}

        for a,b in prerequisites:
            indegree[a] += 1 
            adj_list[b].append(a)  
         
        queue = deque()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i)
        
        course_count = 0 
        while queue:
            
            current = queue.popleft()
            course_count += 1 

            sorted_order.append(current)
            for neighbour in adj_list[current]:
                indegree[neighbour] -= 1
                if indegree[neighbour] == 0:
                    queue.append(neighbour)

        if course_count == numCourses:
            return sorted_order

        else:
            return []
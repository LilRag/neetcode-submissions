class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        from collections import deque

        indegree =[0]*numCourses
        adj_list ={i:[] for i in range(numCourses)}

        for a,b in prerequisites:
            indegree[a] += 1 
            adj_list[b].append(a)   

        
        queue = deque()

        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i)
            
        courses_taken = 0 
        while queue:
            current = queue.popleft()
            courses_taken += 1 
            for neighbour in adj_list[current]:
                indegree[neighbour] -= 1
                if indegree[neighbour] == 0:
                    queue.append(neighbour)

        if courses_taken == numCourses:
            return True

        else:
            return False
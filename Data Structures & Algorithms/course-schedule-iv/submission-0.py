class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        from collections import defaultdict
        from collections import deque 

        master_map ={}
        adj_list = defaultdict(list)

        for u,v in prerequisites:
            adj_list[u].append(v)   


        for i in range(numCourses):
            queue = deque([i])
            visited = set()

            while queue:
                curr = queue.popleft()
                for nbr in adj_list[curr]:
                    if nbr not in visited:
                        visited.add(nbr)
                        queue.append(nbr)

            master_map[i] = visited

        answer = []

        for x,y in queries:
            if y in master_map[x]:
                answer.append(True)
            else:
                answer.append(False)


        return answer
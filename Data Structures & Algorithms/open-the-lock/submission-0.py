class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        from collections import deque

        queue = deque()
        visited = set(deadends) 

        if "0000" in visited:
            return -1 

            
        queue = deque([("0000", 0)]) #current_lock , turns 
        visited.add("0000")


        def get_neighbours(lock_state):
            neighbours =[]

            for i in range(4):
                digit = int(lock_state[i])

                up_digit = str((digit + 1)%10)
                down_digit = str((digit - 1)%10)

                up_state = lock_state[:i] + up_digit + lock_state[i+1:]
                down_state = lock_state[:i] + down_digit + lock_state[i+1:]
                
                neighbours.append(up_state)
                neighbours.append(down_state)

            return neighbours 

        

        while queue: 
            current, turns = queue.popleft()

            if current == target:
                return turns 
            
            nbrs = get_neighbours(current)

            for nbr in nbrs:
                if nbr not in visited:
                    visited.add(nbr)
                    queue.append((nbr,turns+1))
        
        return -1 



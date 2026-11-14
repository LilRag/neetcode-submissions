class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # goal: have we reached a valid state, if yes append a deep copy to res 
        # choices: loop through all available options from current state 
        # constraints , pruning 
        # choose -> explore -> unchoose 


        # so here the goal is possible permutations, 
        # our possible choices are defined by the nums array 
        # first permutation is the same array 
        # we maintain a used set for each iteration 
        # after we have exhausted the use set , we back track , choose different options 

        res = []

        def backtrack(current_path, used):
            if len(current_path) == len(nums):
                # append a copy (current_path[:]) not the reference 
                res.append(current_path[:])
                return 
            
            for num in nums:
                if num in used:
                    continue 

                used.add(num)
                current_path.append(num)

                backtrack(current_path, used)

                current_path.pop()
                used.remove(num)

        backtrack([],set())
        return res 
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # for each step i 
        # the minimum cost to reach the top is 
        # cost[i] + min cost to step i+1 or i+2

        # memo array stores the minimum cost to reach the top from step i 
        # dfs(i)
        # if i is beyond the last step, return 0 
        # if memo[i] is already computed return it 
        # start from step 0 or step 1 

        memo = [-1]*(len(cost))

        def dfs(i):
            if i >= len(cost):
                return 0 

            if memo[i] != -1:
                return memo[i]

            memo[i] = cost[i] + min(dfs(i+1), dfs(i+2))
            return memo[i]

        return min(dfs(0),dfs(1))
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # cost[i] is the cost of taking a step from ith floor of a staircase
        # you can either step to i+1 th floor or i+2th floor

        N = len(cost)
  
        for i in range(2, N):
            cost[i] += min(cost[i - 1], cost[i - 2])

        return min(cost[N - 1], cost[N - 2])
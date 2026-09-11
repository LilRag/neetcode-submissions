class Solution:
    def climbStairs(self, n: int) -> int:

        def ways(n,memo = {}):
            if n <= 1:
                return 1

            if n in memo:
                return memo[n]
            memo[n] = ways(n-1, memo) + ways(n-2, memo)
            return memo[n]

        return ways(n)
class Solution:
    def climbStairs(self, n: int) -> int:
        # 1D dp, recursion with memory over a single changing state 
        # instead of recomputing overlapping subproblems exponentially 
        # store answers in a 1D array dp so each state is solved once

        # define state dp[i]
        # if im at state i, what previous states could i come from 
        # base case , dp[0]
        #

        # integer n , represents number of steps to reach the top of a staircase 
        # at a time we can climb either 1 or 2 steps at a time 
        # return number of way to climb 
        # so it will be either 1 + 1 step or direct 2 
        # 2 ways 

        # n = 3 , 1 + 1 + 1 = 3 ; 1 + 2 = 3 ; 2 + 1 = 3
        # at each stage our choices are either 1 or 2 

        # to reach dp[i] , we would have to come from dp[i-1] or dp[i-2]
        # add these as two sets of paths are disjoint , the total count is 
        # dp[i] = dp[i-1] + dp[i-2]
        # base case dp[1] = 1 ; dp[2] = 2 

        # naive solution doesnt store answers 
        # if n <= 2:
        #     return n

        # else: 
        #     return self.climbStairs(n-1) + self.climbStairs(n-2)

        # computes results multiple times (O n^2)

        dp = [0]*(n+1)

        if n<=2 :
            return n 

        dp[1] = 1 
        dp[2] = 2 

        for i in range(3,n+1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n]
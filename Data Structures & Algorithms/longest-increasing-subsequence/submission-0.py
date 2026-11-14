class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # we have an integer array 
        # we need to return the length of the longest strictly increasing subsequence 
        # subsquence -> sequence that can be derived from any sequence by deleting some or no elements without chaning the relative order 

        # [9,1,4,2,3,3,7] -> [1,2,3,7]
        # [0,3,1,3,2,3] -> [0,1,2,3]

        # LIS[n]
        # LIS[n] = 1 + max{LIS[K] | k < n, A[k] < A[n]}

        # base case LIS[0] = 1 
        # every element statrs with a default value of 1 
        
        #LIS[n] = 1 + max{{0} U LIS[K] | k < n, A[k] < A[n]}

        if not nums:
            return 0 

        n = len(nums)
        LIS = [1]*n

        for n in range(1,n):
            candidates = [LIS[k] for k in range(n) if nums[k] < nums[n]]
            LIS[n] = 1 + max(candidates, default = 0)

        return max(LIS) 
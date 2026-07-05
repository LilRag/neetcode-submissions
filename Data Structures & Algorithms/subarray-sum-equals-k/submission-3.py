class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0 
        cur_sum = 0 
        prefixSum = {0:1}

        for n in nums:
            cur_sum += n 
            diff = cur_sum - k 

            res += prefixSum.get(diff, 0)
            prefixSum[cur_sum] = 1 + prefixSum.get(cur_sum, 0)

        return res
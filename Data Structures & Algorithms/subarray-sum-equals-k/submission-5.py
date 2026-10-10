class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0 
        cur_sum = 0 
        prefix_sum = {0:1}
        

        for i in range(len(nums)):
            cur_sum += nums[i]
            diff_sum =  cur_sum - k 

            res += prefix_sum.get(diff_sum , 0)
            prefix_sum[cur_sum] = 1 + prefix_sum.get(cur_sum, 0) 
        
        return res
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = 0
        n = len(nums) 
        for i in range(len(nums)):
            cnt = 0 
            for j in range(i,n):
                if nums[j] == 0: break
                cnt += 1

            max_count = max(max_count, cnt)

        return max_count 

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        nums = list(dict.fromkeys(nums))
        
        max_count = 1
        count = 1
        if len(nums) < 1:
            return 0 


        for i in range(len(nums)-1):
            if nums[i+1] == nums[i] + 1:
                count += 1 
                print(count)
            else: 
                if max_count < count: 
                    max_count = count
                count = 1 
        if max_count < count: 
                max_count = count

        return max_count 

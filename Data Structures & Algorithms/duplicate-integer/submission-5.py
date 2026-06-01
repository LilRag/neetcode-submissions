class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count ={}
        output = 0 
        for i in range(len(nums)): 
            count[nums[i]] = count.get(nums[i], 0)+1
        
        for i in count:
            if count[i] == 1:
                continue
            else:
                output = 1 

        if output == 0:
            return False
        else:
            return True 

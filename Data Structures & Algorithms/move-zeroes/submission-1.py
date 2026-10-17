class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """ 
        l = 0

        for r in range(len(nums)):
            if nums[r] != 0:
                if nums[l] != 0:
                    r += 1
                    l +=1 
                else:
                    nums[l] = nums[r]
                    nums[r] = 0
                    l += 1 


                

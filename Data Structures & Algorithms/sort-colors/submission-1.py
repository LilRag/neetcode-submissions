class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # same color grouped together 
        cr = 0
        cw = 0 
        cb = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                cr += 1 
            elif nums[i] == 1: 
                cw += 1 
            else:
                cb +=1 
        
        idx = 0 
        
        for i in range(cr):
            nums[idx] = 0
            idx += 1 

        for i in range(cw):
            nums[idx] = 1
            idx +=1 

        for i in range(cb):
            nums[idx] = 2
            idx +=1 
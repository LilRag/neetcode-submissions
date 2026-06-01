class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c0 = 0 
        c1 = 0 
        c2 = 0 

        for num in nums :
            if num == 0:
                c0 +=1 

            if num == 1:
                c1 += 1 
            
            if num == 2:
                c2 += 1

        idx = 0 
        for i in range(c0):
            nums[idx] = 0 
            idx +=1 

        for i in range(c1):
            nums[idx] = 1
            idx +=1 

        for i in range(c2):
            nums[idx] = 2
            idx +=1 

        return nums
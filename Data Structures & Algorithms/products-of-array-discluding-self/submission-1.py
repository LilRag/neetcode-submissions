class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # by division 

        zero_cnt = 0 
        res =[0]*len(nums)
        prod = 1 
        for i in range(len(nums)):
            if nums[i] == 0:
                zero_cnt +=1
            else:
                prod *= nums[i]
        if zero_cnt > 1 : return [0]*len(nums)

        for i,c in enumerate(nums):
            if zero_cnt: res[i] = 0 if c else prod 
            else: res[i] = prod//c

        return res

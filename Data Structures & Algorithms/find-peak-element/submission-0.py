class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # ig we check all the local peaks and update it if we find a better local peak 

        left = 0 
        right = len(nums) - 1 

        while left < right:
            mid = (left+right)//2

            # upward slope
            if nums[mid] < nums[mid+1]:
                left = mid + 1 

            else:
               right = mid
            
        return left
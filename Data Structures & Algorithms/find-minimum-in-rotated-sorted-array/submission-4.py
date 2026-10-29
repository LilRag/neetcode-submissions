class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]

        left = 0 
        right = len(nums) -1 

        while left <= right:
            

            if nums[left] < nums[right]:
                # already in sorted order
                res = min(res, nums[left])
                break

            mid = (left + right) //2
            res =  min(res, nums[mid])
            if nums[left] <= nums[mid]:
                # we are in the large half 
                # move to the right half 
                left = mid + 1 

            else:
                right = mid - 1 


        return res
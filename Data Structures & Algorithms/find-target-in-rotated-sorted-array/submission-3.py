class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l , r = 0 , len(nums) - 1 

        while l < r: 
            m = (l + r)//2
            if nums[m] > nums[r]:
                l = m + 1 
            else:
                r = m 

        pivot = l 

        def binary_search(left, right):
            while left <= right:
                mid = (left + right) //2

                if target == nums[mid]:
                    return mid 

                elif target > nums[mid]:
                    left = mid + 1 

                else:
                    right = mid - 1 

            return -1 


        if pivot > 0 and nums[0] <= target <= nums[pivot - 1]:
            return binary_search(0, pivot - 1)

        else:
            return binary_search(pivot, len(nums)-1)
        
        

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        #[3,4,5,6,1,2]
        # we have to find the drop off i.e the min 
        # 5 > 2, search right half  
        # l = 3 r = 5 
        # 1 < 2 ; r = 4 
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m

        pivot = l

        def binary_search(left: int, right: int) -> int:
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1

        if pivot > 0 and nums[0] <= target <= nums[pivot -1]:
            # first half 
            return binary_search(0, pivot -1)

        else:
            return binary_search(pivot, len(nums)-1 )
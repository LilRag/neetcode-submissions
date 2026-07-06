class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        nums2 = set(nums)

        if n != len(nums2):
            return True

        else: 
            return False 
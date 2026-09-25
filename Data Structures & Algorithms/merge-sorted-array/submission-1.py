class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # nums1 has empty spaces in the end 
        # what if we replaced the inplace elements from nums2 
        # then run sorting on top of it 
        # what is the optimal way to find 0 and replace with nums2

        nums1[m:] = nums2

        nums1.sort() 
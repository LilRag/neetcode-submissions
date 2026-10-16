class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        merged = defaultdict(int)
    
        # Add values from both arrays
        for id_, val in nums1 + nums2:
            merged[id_] += val
            
        # Return as a sorted 2D array
        return sorted([[id_, val] for id_, val in merged.items()])

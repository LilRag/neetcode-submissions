class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        from itertools import combinations 
        subsets = []
        for r in range(len(nums)+1):
            for subset in combinations(nums, r):
                subsets.append(list(subset))

    
        return subsets
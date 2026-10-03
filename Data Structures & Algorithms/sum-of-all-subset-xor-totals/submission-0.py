class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        # xor total -> bitwise xor of all its elements, or 0 if array is empty  
        from itertools import combinations, permutations
        total_sum = 0 
        for r in range(1, len(nums) + 1):
            for subset in combinations(nums, r):
                current_xor = 0 

                for num in subset:
                    current_xor ^= num

                total_sum += current_xor

        return total_sum
        
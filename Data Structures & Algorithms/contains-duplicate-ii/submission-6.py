class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashmap = {}
        for i, a in enumerate(nums):
            if a in hashmap and i - hashmap[a] <= k:
                return True
            hashmap[a] = i  # Always update to the latest index!
            
        return False
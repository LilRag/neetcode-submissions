from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # Base case
        if len(nums) <= 1: 
            return nums
        
        mid = len(nums) // 2 
        left_half = nums[:mid]
        right_half = nums[mid:]

        # Added 'self.' since sortArray is a class method
        left_sorted = self.sortArray(left_half)
        right_sorted = self.sortArray(right_half)

        # Added 'self.' to call the class method
        return self.merge(left_sorted, right_sorted) 

    # Added 'self' as the first parameter
    def merge(self, left: List[int], right: List[int]) -> List[int]:
        sorted_array = []
        i = 0 
        j = 0 

        while i < len(left) and j < len(right):
            # FIXED: Compare left[i] with right[j], not right[i]
            if left[i] < right[j]:
                sorted_array.append(left[i])
                i += 1 
            else:
                sorted_array.append(right[j])
                j += 1

        # Append any remaining elements
        sorted_array.extend(left[i:])
        sorted_array.extend(right[j:])

        return sorted_array
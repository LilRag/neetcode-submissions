class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index1 = []
        low = 0 
        while low < len(numbers):
            rem = target - numbers[low]
            if rem in numbers:
                index1.append(low+1)
                index1.append((numbers.index(rem))+1)
                break 
            else:
                low += 1 
            
        return index1 
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # no O(N) extra space (no sets, dict)
        # creating a copy or slice of an array creates a new buffer of size N

        # two pointer logic? 
        # sum = 10 
        # 1 and 4 , 5 target = 3 
        # for a smaller total we must move the right pointer inward
        # 1 , 3 = 4 
        # continue 
        # 1 , 2 


        #[2, 4, 6, 8, 10 , 12]
        # 9 
        # 2 and 12 > 14 
        # 2 and 10 > 12 
        # 2 and 8 > 10 
        # 2 and 6 > 8 
        # 4 and 6 > 10  
        # not possible

        left = 0 
        right = len(numbers) - 1

        while left <= right:
            if numbers[left] + numbers[right] == target:
                return [left + 1 , right + 1 ]

            elif numbers[left] + numbers[right] < target:
                left += 1 

            else:
                right -= 1 

        
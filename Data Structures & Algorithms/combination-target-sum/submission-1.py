class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(index: int , current: List[int] , target: int):

            if target == 0:
                result.append(current[:])
                return 

            if target < 0 or index == len(nums):
                return []

            
            dfs(index , current + [nums[index]] , target - nums[index])

            dfs(index + 1 , current , target)

        
    
        dfs(0,[], target)
        return result
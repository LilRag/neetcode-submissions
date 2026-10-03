class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # same logic 
        # dfs include and exclude 
        # we can set the target, do the subraction and when we hit zero thats our success condition 
        # if the value drops below  
        result = []

        def dfs(index: int , current: List[int] , target ): 

            if target == 0:
                result.append(current[:])
                return 

            if target < 0 or index == len(nums):
                return 

            # include 
            dfs(index, current + [nums[index]] , target - nums[index])

            # exclude
            dfs(index + 1 , current, target)


        dfs(0,[], target)

        return result
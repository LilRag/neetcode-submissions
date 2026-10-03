class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        def dfs(index:int , current: List[int]):
            # base condition 
            if index == len(nums):
                result.append(current[:])
                return 

            #include 
            dfs(index + 1, current + [nums[index]])
            # exclude 
            dfs(index + 1, current)

        dfs(0, [])

        return result
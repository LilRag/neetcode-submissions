class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # 1. Sort to group duplicates together so we can easily skip them
        candidates.sort()
        result = []

        def dfs(index: int, current: List[int], target: int):
            if target == 0:
                result.append(current[:])
                return
            if target < 0:
                return

            # 2. Iterate through the remaining candidates
            for i in range(index, len(candidates)):
                
                # 3. THE MAGIC LINE: Skip duplicates at the same tree level!
                # If 'i > index', it means this is not the first branch we are 
                # drawing from this node. If it's the same value as the previous 
                # branch, skip it to avoid duplicate combinations.
                if i > index and candidates[i] == candidates[i - 1]:
                    continue
                
                # Choose
                current.append(candidates[i])
                
                # Explore (pass i + 1 so we don't reuse the exact same element)
                dfs(i + 1, current, target - candidates[i])
                
                # Un-choose (Backtrack)
                current.pop()

        dfs(0, [], target)
        return result
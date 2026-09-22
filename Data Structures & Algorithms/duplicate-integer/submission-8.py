class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = {}
        output = 0 
        for i in nums:
            count[i] = count.get(i, 0)+1


        for i in count.keys():
            if count[i] == 1:
                continue
            else:
                output =1 

        if output == 0:
            return False

        else:
            return True
            
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        score = {}
        res = []
        n = len(nums)
        for num in nums:
            score[num] = score.get(num , 0) + 1 
        
        for key,value  in score.items():
            if value > n/3:
                res.append(key)

        return res
    
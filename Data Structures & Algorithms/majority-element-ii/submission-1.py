class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)

        count = {}
        output = []

        for i in range(n):
            count[nums[i]] = count.get(nums[i], 0) + 1

        for key,value in count.items():
            if value > n/3:
                output.append(key)

        return output 

        
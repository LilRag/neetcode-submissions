class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        list1 = []
        for i in range(len(nums)):
            count[nums[i]] = count.get(nums[i], 0) + 1

        while k > 0:
            print(count)
            max_val = max(count , key = lambda k: count[k]) 
            print(max_val)
            list1.append(max_val)
            count.pop(max_val)
            k -= 1 
        return list1
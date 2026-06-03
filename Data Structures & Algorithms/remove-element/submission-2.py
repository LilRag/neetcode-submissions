class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # remove all occurrences of val in nums in-place 
        # order may be changes, return no. of elements in nums which are not equal to val 
        
        temp = []
        for num in nums:
            if num == val:
                continue 
            temp.append(num)
        for i in range(len(temp)):
            nums[i] = temp[i]
        return len(temp)
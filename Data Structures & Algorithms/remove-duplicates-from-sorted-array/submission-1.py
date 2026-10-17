class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0 

        write_index = 1 

        for read_index in range(1, len(nums)):
            if nums[read_index] != nums[read_index - 1]:
                nums[write_index] = nums[read_index]
                write_index += 1 
                print(write_index)

        return write_index
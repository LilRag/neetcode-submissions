class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # convert to list 
        # find the last non empty string
        # take the count 

        split_list = s.split()
        
        return len(split_list[-1])
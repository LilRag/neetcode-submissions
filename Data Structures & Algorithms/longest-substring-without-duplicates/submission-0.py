class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window approach 
        # left and right , increment right until we see new char 
        # we update max value with every movement of a new character to a valid window  
        # and then move the left pointer until we skip all duplicates 

        char_set = set()
        left = 0 
        max_length = 0 


        for right in range(len(s)):
            # if we see a duplicate, we shrink the window from the left unitl its gone
            while s[right] in char_set: 
                char_set.remove(s[left])
                left += 1 

            char_set.add(s[right])
            max_length = max(max_length, right - left + 1 )

        return max_length 
                        

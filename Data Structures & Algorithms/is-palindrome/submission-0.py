class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower_s = s.lower()
        no_whitespace = "".join(lower_s.split())
        filtered = "".join(filter(str.isalnum,no_whitespace))

        left = 0 
        right = len(filtered) -1 
        while left < right:
            if filtered[left] != filtered[right]:
                    return False
            left += 1 
            right -= 1 

        return True 
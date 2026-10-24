class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = "".join(s.split())
        cleaned_s = ""
        for i in range(len(s)):
            if s[i].isalnum():
                cleaned_s += s[i] 

        left = 0 
        right = len(cleaned_s) - 1

        while left <= right:
            if cleaned_s[left] != cleaned_s[right]:
                return False
            else:
                left +=1 
                right -= 1 

        return True 
            
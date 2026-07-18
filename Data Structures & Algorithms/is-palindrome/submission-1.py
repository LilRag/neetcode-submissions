class Solution:
    def isPalindrome(self, s: str) -> bool:
        preproc = s.replace(" ","")
        cleaned = ""
        for i in preproc:
            if i.isalnum():
                cleaned +=i 

        lcleaned = cleaned.lower()

        for i in range(len(lcleaned)):
            if lcleaned[i] != lcleaned[len(lcleaned) - 1 -i ]:
                return False

        return True  
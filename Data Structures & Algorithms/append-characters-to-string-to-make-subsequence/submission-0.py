class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        # so we need to check if t is a subsequence of s first 
        # if not , we would have to keep track of how characters that are already present 
        # then remaining must be added to the subsequence 

        # when we checked the subsequence , we set two pointers 
        # moved the pointer only when matching 
        # so over here if it full matches we set it as 0 
        # if it doesnt , from wherever the t pointer is till its end we add that much to s (we can just count the remaining and return)
        if not t:
            return 0 
        
        pt, ps = 0,0 

        count = 0

        # we are checking if t is a subsequence 

        for ps in range(len(s)):
            if s[ps] == t[pt]: 
                pt += 1 

            if len(t) == pt:
                return 0 

        count = len(t) - pt

        return count 
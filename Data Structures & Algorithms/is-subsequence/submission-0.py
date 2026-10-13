class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # relative position cannot be distrubed
        # chars of s must be in t 
        # what if i get all the chars in s
        # then checked their indexes in t 
        
        if not s:
            return True

        pt,ps = 0 ,0 

        n = len(s)

        for pt in range(len(t)):
            if t[pt] == s[ps]:
                ps += 1

            if ps == n:
                return True

    
        return False 

             
            

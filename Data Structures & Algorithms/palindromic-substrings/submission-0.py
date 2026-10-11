class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        

        # helper function to expand outward from a given center
        def countPali(left,right):
            count = 0 
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count +=1 
                left -= 1 
                right += 1 

            return count 

        
        for i in range(len(s)):
            # count odd palidromes 
            res += countPali(i,i)  
            res += countPali(i,i+1)

        return res  
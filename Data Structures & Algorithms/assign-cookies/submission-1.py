class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        res = 0
        
        g.sort(reverse = True)

        for i in range(len(g)):
            if s:
                if g[i] <= max(s):
                    res +=1  
                    s.remove(max(s))
            else:
                break 

        return res
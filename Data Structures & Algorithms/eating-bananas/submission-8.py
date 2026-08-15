import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        l = 1 
        r = max(piles)
        min_eating = float('inf')
        while l <= r:
            k = (l+r)//2
            count = 0
            hours = 0 
            for i in piles:
                hours += math.ceil(i/k)
            if hours <= h: 
                min_eating = min(min_eating, k)
                r = k - 1 
            else:            
                l = k + 1 

        return min_eating
            

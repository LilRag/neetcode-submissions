class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)
        res = r

        def canShip(cap):
            ships, currCap = 1, cap 
            for w in weights:
                if currCap - w < 0:
                    ships += 1 
                    currCap = cap 
                currCap -= w 

            return ships <= days 


        while l <= r :
            k = (l+r)//2
            if canShip(k):
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1 

        return res 
                      

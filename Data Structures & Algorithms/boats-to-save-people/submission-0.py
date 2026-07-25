class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l, r = 0 , len(people) -1 
        
        res = 0 # number of boats

        while l<=r: 
            remainder = limit - people[r]
            r -= 1 
            res += 1 
            if l <= r and remainder >= people[l]:
                l += 1 
        return res 

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # shipped from one port to another in days 
        # ith package has weights[i]
        # load ship with packages 
        # dont load more than max capacity of ship
        # return least weight capacity of ship 

        #lower bound, a single package cannot be split, ship must have atleast capacity of max 
        # upper bound , if the capacity is the sum of all it can carry everything in one day 

        # if c capacity can ship in d days
        # any c1 > c can ship in =< d days 

        def can_ship(capacity: int):
            needed_days = 1 
            current_load = 0 

            for w in weights:
                if current_load + w > capacity:
                    needed_days += 1 
                    current_load = 0 
                current_load += w 

            return needed_days <= days 

        
        low = max(weights)
        high = sum(weights)

        while low < high:
            mid = (low+ high)//2
            if can_ship(mid):
                high = mid 

            else:
                low = mid + 1 

        return low
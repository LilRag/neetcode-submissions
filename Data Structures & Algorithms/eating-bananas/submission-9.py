class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # pilies is the number of bananas in the ith piles
        # h is number of hours you have to eat all bananas
        # decide banana eating rate k 
        # each hour we can choose to eat that pile , eats k bananas 
        # if pile has less than k , we can finish but we cant choose another pile in the same hour 


        # piles = [1,4,3,2] h = 9 
        # eating rate 1, 1 + 4 + 3 + 2 = 10 
        # eating rate 4 , 1 + 1 + 1 + 1 = 4
        # binary search between minimum and maximum eating rate that should be the closest to the target hours 
        # but we also need to calculate the hours at a given k value right

        import math 

        n = len(piles)
        l = 1 
        r = max(piles)
        min_eating = math.inf

        while l<=r:
            k = (l+r)//2
            hours = 0 
            for i in piles:
                hours += math.ceil(i/k)

            if hours <= h:
                r = k - 1 
                min_eating = min(min_eating, k)
            else:
                l = k + 1 

        return min_eating
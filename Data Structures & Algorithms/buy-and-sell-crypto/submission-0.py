class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # sliding window 
        # so i must look for a day when its low and then look for the next day thats maximum
        # its only a single transaction 

        max_profit = 0     
        min_price = prices[0]

        for i in range(len(prices)):
            min_price = min(prices[i], min_price)

            profit = prices[i] - min_price 

            max_profit = max(profit, max_profit)

        return max_profit 
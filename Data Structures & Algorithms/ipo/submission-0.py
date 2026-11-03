class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # finish k projects before IPO 
        # maximize the capital 
        # initial capital w, profits added to w when project completed 
        # capital[i] is the min required to start the project 
        # [0,3,1] w = 8
        # single heap doesnt , work as we would need to pick index that gives max profit 
        # sort projects by capital and profit
        # use a max heap for profits 
        # pop max profit add it to w and decrement k 

        projects = sorted(zip(capital, profits))

        max_profit = []
        i = 0 
        n = len(capital)
        for _ in range(k):
            while i < n and projects[i][0] <= w:
                heapq.heappush(max_profit, -projects[i][1])
                i += 1 
            # if no projects can be afforded , stop early 
            if not max_profit:
                break

            w += -heapq.heappop(max_profit)

        return w
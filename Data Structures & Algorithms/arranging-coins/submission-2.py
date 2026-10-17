class Solution:
    def arrangeCoins(self, n: int) -> int:
        # so we have to basically maintain the count , 1 , 2 , 3 ...    
        # for each row , we subtract that number from n , if its possible , we add one to the result (count correct rows formed)
        res = 0 
        i = 0 
        for i in range(1, n + 1):
            if n >= i:
                n -= i 
                res += 1 
            else:
                break 

        return res 
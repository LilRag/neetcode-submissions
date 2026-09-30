class Solution:
    def hammingWeight(self, n: int) -> int:
        res = ""
        while n >= 1:
            rem = n%2
            res += str(rem)
            n = n // 2 
        
        count =0 
        for i in res:
            if i =="1":
                count += 1 

        return count
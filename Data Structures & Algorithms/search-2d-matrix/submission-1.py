class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # row is sorted in non decreasing order 
        # first integer of every row is greater than the last integer 

        # to find a target 10 
        # we find the correct row, by looking at the first of element of the first column 
        # then when we find the row , we do search the row 


        row_len = len(matrix) # rows
        col_len = len(matrix[0]) # cols 

        top = 0 
        bot = row_len - 1 

        while top <= bot:
            row = (top + bot)//2

            if target > matrix[row][-1]:
                top = row + 1  

            elif target < matrix[row][0]:
                bot = row - 1 

            else:
                break 

        if not (top <= bot):
            return False

        row = (top + bot)//2 
        
        l = 0 
        r = col_len - 1 

        while l <= r:
            m = (l + r)//2
            if matrix[row][m] > target:
                r = m - 1 
            elif matrix[row][m] < target:
                l = m + 1
            else:
                return True 
        return False 
                    
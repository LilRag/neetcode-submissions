class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        
        intervals.sort(key = lambda x:x[0])
        res =[intervals[0]]
        # merge all overlapping
        # return array of non overlapping that covers all
    
        for i in range(1, len(intervals)):
            last_added = res[-1]
            current_interval = intervals[i]

            # for overlap 
            if current_interval[0] <= last_added[1]:
                last_added[1] = max(last_added[1], current_interval[1])
            # non overlap 
            else:
                res.append(current_interval)

        return res    

            

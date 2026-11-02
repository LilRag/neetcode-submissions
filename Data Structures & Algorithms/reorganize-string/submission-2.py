class Solution:
    def reorganizeString(self, s: str) -> str:
        #two adjacent characters are not the same
        # axyy -> yxay
        # abbccdd -> abcdbcd
    
        #max heap , with frequency of each letter? 
        #pop it out
        # store it
        # push another to the max position and then repeat
        # but we need to subtract to the frequency and add it back to the list 


        counts = Counter(s)
        n = len(s)

        max_freq = max(counts.values())
        if max_freq > (n+1)//2:
            return ""

        max_heap = [(-freq, char) for char, freq in counts.items()]
        heapq.heapify(max_heap)

        prev_freq, prev_char = 0, ""
        res = []

        while max_heap:
            freq, char = heapq.heappop(max_heap)
            res.append(char)

            if prev_freq < 0:
                heapq.heappush(max_heap ,(prev_freq, prev_char))

            prev_freq =freq + 1
            prev_char = char 

        return "".join(res)
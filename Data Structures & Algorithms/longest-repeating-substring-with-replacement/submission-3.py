class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0 
        count ={}
        max_length = 0 

        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            max_f = max(count.values())
            length_window = right - left + 1
            if length_window > max_f:  
                replacements_required = length_window - max_f
                if replacements_required > k:
                    count[s[left]] -= 1
                    left += 1 
                    
                else:                
                    max_length = max(max_length, length_window)
                     

            else:
                max_length = length_window

        return max_length

                

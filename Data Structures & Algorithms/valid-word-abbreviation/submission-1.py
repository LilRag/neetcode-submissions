class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = 0  # pointer in word
        j = 0  # pointer in abbr
        n = len(word)
        m = len(abbr)
        
        while i < n and j < m:
            if abbr[j].isdigit():
                # Invalid if it starts with '0' (leading zero or empty substring)
                if abbr[j] == '0':
                    return False
                
                # Parse the full number
                num = 0
                while j < m and abbr[j].isdigit():
                    num = num * 10 + int(abbr[j])
                    j += 1
                
                # Advance the word pointer by the parsed number
                i += num
            else:
                # If characters do not match
                if word[i] != abbr[j]:
                    return False
                i += 1
                j += 1
        
        # Valid only if both strings are fully traversed
        return i == n and j == m



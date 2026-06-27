class Solution:

    def encode(self, strs: List[str]) -> str:
        for i in range(len(strs)):
            strs[i] = str(len(strs[i])) + '#' + strs[i]
        result = "".join(strs)
        return result 

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        
        while i < len(s):
            # 1. Use a secondary pointer 'j' to find the next '#'
            j = i
            while s[j] != '#':
                j += 1
            
            # 2. Extract the length (this safely handles multi-digit numbers like 10, 100, etc.)
            length = int(s[i:j])
            
            # 3. Extract the actual string
            # j is the index of '#', so the string starts at j+1 and ends at j+1+length
            word = s[j+1 : j+1+length]
            result.append(word)
            
            # 4. Move the main pointer 'i' to the start of the next encoded string
            i = j + 1 + length
            
        return result
    
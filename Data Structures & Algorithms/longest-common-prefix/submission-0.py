class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        shortest = min(strs, key = len )

        for i in range(len(shortest)):
            character_to_match = shortest[i]

            for s in strs:
                if s[i] != character_to_match:
                    return shortest[:i]
            
        return shortest
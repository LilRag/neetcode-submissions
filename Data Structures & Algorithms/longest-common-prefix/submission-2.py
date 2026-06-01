class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        short = min(strs)
        
        for i in range(len(short)):
            char_to_match = short[i]

            for s in strs:
                if s[i] != char_to_match:
                    return short[:i]

        return short
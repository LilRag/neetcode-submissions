class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        short = min(strs)
        output = ""

        for i in range(len(short)):
            chars_to_match = short[i]

            for s in strs:
                if s[i] != chars_to_match:
                    return s[:i]

        return short
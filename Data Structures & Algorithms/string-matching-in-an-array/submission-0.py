class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        # find the smallest words 
        # check if its a substring of a larger word
        # pop it out to a result set it if it is 
        # repeat until no element left 
        words.sort(key = len)
        res =[]

        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if words[i] in words[j]:
                    res.append(words[i])

                    break

        return res
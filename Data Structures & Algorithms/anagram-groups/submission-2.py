class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Sorting method 
        # each key is a sorted version of a string and value is list of strings that belong to that group
        res = defaultdict(list)
        for s in strs:
            sortedS = ''.join(sorted(s)) # sort each character in a  word alphabetically 
            res[sortedS].append(s)
        return list(res.values())


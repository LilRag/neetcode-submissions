class TrieNode:
    def __init__(self):
        self.children= {}
        self.end_of_word = False 
  
class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        # they give you string 
        # a dictionary 
        # goal is to cover as much of string s as possible using words from dictionary 
        # without overlapping them, and count how many left uncovered 
        
        # add all the words to the trie from the dictionary 
        root = TrieNode()
        for word in dictionary:
            curr = root
            for char in word:
                if char not in curr.children:
                    curr.children[char]= TrieNode()
                curr = curr.children[char]
            curr.end_of_word = True 

        

        # from index i we walk down the trie character by character (j = i + 1 .. )
        # everytime we hit a node with end_of_word , we found a valid dictionary word
        # so we have to jump to dfs(j + 1)
        # the moment s[j] isnt in curr.children , we stop the inner loop , as no word stars with that prefix 

        memo = {}
        
        def dfs(i):
            
            if i == len(s):
                return 0 

            if i in memo:
                return memo[i]

            # choice 1: skip s[i] (count it as 1 extra char , next call starts at root)
            res = 1 + dfs(i+1)

            # choice 2: start fresh at root and look for words starting at index i 
            curr = root 
            for j in range(i, len(s)):
                if s[j] not in curr.children:
                    break
                curr = curr.children[s[j]]
                if curr.end_of_word:
                    # found a valid word s[i..j] jump to j + 1 which starts at root 
                    res = min(res, dfs(j + 1))
            memo[i] = res 

            return res 

        return dfs(0)
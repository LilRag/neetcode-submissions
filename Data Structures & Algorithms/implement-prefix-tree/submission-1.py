class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False 


class PrefixTree:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word:str)->None:
        curr = self.root 

        for c in word:
            if c not in curr.children:  # if character does not exist , hasnt been inserted
                curr.children[c] = TrieNode() # create a trie node for the character 
            curr = curr.children[c] # if the character already exists in the trie , set curr to that child and continue with next character 
        curr.endOfWord = True 

    def search(self, word:str)->bool:
        curr = self.root 
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.endOfWord

    def startsWith(self, prefix:str)->bool:
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True 
        
        
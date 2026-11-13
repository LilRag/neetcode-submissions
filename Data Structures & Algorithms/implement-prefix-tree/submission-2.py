class PrefixTreeNode:
    def  __init__(self):
        self.children = {}
        self.is_end_of_word = False


class PrefixTree:
# trie starts with an empty root node 
# from the root , paths branch out to child nodes , representing next chars
# each node contains 
    # 1. a mapping pointing to its child nodes, an array of size 26 for lowercase english letters 
    # 2. a boolean flag , indicating whether the path from root to this node , completes a valid word 


    def __init__(self):
        self.root = PrefixTreeNode()


    def insert(self, word: str) -> None:
        # start at root node
        # for each char in the word, check if a child node for that char exists, if not create one 
        # move down to that child node
        # once all characters are processed , mark the current nodes' boolean flag as true 
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = PrefixTreeNode()
            curr = curr.children[char]
        curr.is_end_of_word = True 

    def search(self, word: str) -> bool:
        # traverse down the tree following the characters of the largest word
        # if a required character edge is missing at any step, the word does not exist return false
        # if you reach the end of the word and return the boolean flag 
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return curr.is_end_of_word


    def startsWith(self, prefix: str) -> bool:
        # similar to exact search, we traverse all characters of the prefix, we return true immediately 
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return True 


    #def deletion(self, prefix:str):
        # search down to the final char of the word and set the boolean to false 
        # back track up the path, deleting nodes if they have no other children and are not the end of another word 



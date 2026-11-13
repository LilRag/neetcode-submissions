class PrefixTree():
    def __init__(self):
        self.children ={}
        self.end_of_word = False 

class WordDictionary:

    def __init__(self):
        self.root = PrefixTree()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = PrefixTree()

            curr = curr.children[char]
        curr.end_of_word = True 

    def search(self, word: str) -> bool:
        def dfs(i: int, node: PrefixTreeNode):
            if i == len(word):
                return node.end_of_word

            char = word[i]
            if char == ".":
                for child in node.children.values():
                    if dfs(i+1, child):
                        return True 
                return False
            else:
                if char not in node.children:
                    return False

                return dfs(i+1, node.children[char])
        return dfs(0,self.root)

        
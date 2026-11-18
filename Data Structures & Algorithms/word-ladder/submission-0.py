class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # begin word 
        # end word 
        # word list 
        # all given words are of the same length, lower case english 

        # transform beginword into endword 
        # we can switch one character in the word, the rest of characters are supposed to remain the same
        # repeat the previous step with the new word that we obtain, do as many times intended 
        # we have to return the number of words within the transformation sequence 


        # so im thinking at each stage we have to match atleast n-1 characters with n-1 characters with any of the words in the list 
        # and when we do we add them to the queue 
        # bfs approach , so we explore the elements in the queue and try to do check if the condition passes 
        # at each stage we must check if we have reached the end word or not and also maintain a count
        # we keep a visited set so we dont repeat already seen words 

        from collections import deque 
        wordSet = set(word for word in wordList)
        
        if endWord not in wordSet:
            return 0 

        queue = deque([(beginWord, 1)])

        while queue:

            word, count  = queue.popleft()

            if word == endWord:
                return count 

            for i in range(len(word)):
                for ch in "abcdefghijklmnopqrstuvwxyz":
                    new_word = word[:i] + ch + word[i+1:]

                    if new_word in wordSet:
                        wordSet.remove(new_word)
                        queue.append((new_word, count+1))

        return 0 
        
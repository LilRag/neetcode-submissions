class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        # two pointer 

        # first we have to remove the spaces 
        # then at every index position we must add that new space 
        # one pointer at the start and one pointer moving , relative index position 
        # on every space added we must account for the shift and move the first pointer accordingly 

        # clean_s = s.replace(" ","")
        # l = 0
        # r= 0 
        # n = len(clean_s)
        # while r < n:
        #     index = r - l 
        #     if index in spaces:
        #         clean_s = clean_s[:r] + " " + clean_s[r:]
        #         spaces.remove(index)
        #         l += 1
        #     r += 1 
        #     n = len(clean_s)

        # return clean_s 

        res = []
        space_idx = 0
        m = len(spaces)

        for i, char in enumerate(s):
            if space_idx < m and i == spaces[space_idx]:
                res.append(" ")
                space_idx +=1 
            res.append(char)

        return "".join(res)
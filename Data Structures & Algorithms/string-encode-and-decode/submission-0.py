class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_list = list(map(lambda x: str(len(x)) + '#' + x, strs))
        combined = ('').join(encoded_list)
        return combined
    def decode(self, s: str) -> List[str]:
        output = [] 
        i = 0 
        total_len = len(s)
        while( i < total_len ):
            pound_index = s.find('#', i)
            length = int(s[i:pound_index])
            output.append(s[pound_index+1: pound_index+length+1])
            i = pound_index +length +1 
        return output
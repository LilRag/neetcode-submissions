class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []  
        
        can_path = path.split("/")
        for token in can_path:
            if token == "" or token == ".": 
                continue
            elif token == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(token)
        
        output = "/"+"/".join(stack)

        return output  

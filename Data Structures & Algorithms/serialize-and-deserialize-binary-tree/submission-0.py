# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        # serialize process of converting an in memory structure into a sequence of bits so that it can be stored or sent across a newtork to be reconstructed later 
        # so i should convert this tree to a string 

        # so when we serealize we can do dfs , we can traverse the tree add the nodes to a result string
        # if we come across a null node, we have a placeholder for null as N 
        res = []
        
        def dfs(node):
            if not node:
                res.append('N')
                return 
            
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(res)
            

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        # reconstructing the serialized content back into its original format 

        # when we deserealize we use dfs for this too , we create nodes for valid nodes 
        # if we hit null we backtrack and return from the current path 

        vals = data.split(",")
        self.i = 0 

        def dfs():
            # base case if null pointer , backtrack
            if vals[self.i] == "N":
                self.i += 1 
                return None

            # create node and increment before recursing 
            node = TreeNode(int(vals[self.i]))
            self.i += 1 

            node.left = dfs()
            node.right = dfs()
            return node 

        return dfs()

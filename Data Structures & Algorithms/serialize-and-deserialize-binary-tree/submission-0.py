# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    '''
    The TSP for this could I guess be make the string root,l,val,r,val ...
    when you receive you parse the same way
    '''
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []

        def dfs(node):
            if not node:
                res.append("N")
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        ans = ",".join(res)
        return ans


        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        res = data.split(",")
        index = [0]
        def dfs():
            if res[index[0]] == "N":
                index[0] += 1
                return None
            node = TreeNode(int(res[index[0]]))
            index[0] += 1
            node.left = dfs()
            node.right = dfs()
            return node
        
        return dfs()


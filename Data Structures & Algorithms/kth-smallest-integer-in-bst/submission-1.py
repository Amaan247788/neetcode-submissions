# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # brute force - do a in order traversal and store every node in a container then return k-1 index
        res = root.val
        count = k
        def inOrderTraversal(root: Optional[TreeNode]) -> None:
            nonlocal count, res
            if not root:
                return
            
            inOrderTraversal(root.left)
            if count == 0:
                return
            count -= 1
            if count == 0:
                res = root.val
                return
            inOrderTraversal(root.right)
        
        inOrderTraversal(root)

        return res


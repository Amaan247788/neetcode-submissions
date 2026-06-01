# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # first find the common root then return if they are the same
        if not subRoot:
            return True
        if not root:
            return False
        
        def isSame(n1: Optional[TreeNode], n2: Optional[TreeNode]) -> bool:
            if not n1 and not n2:
                return True
            if n1 and n2 and n1.val == n2.val:
                return isSame(n1.left, n2.left) and isSame(n1.right, n2.right)
            
            return False
        
        if isSame(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        

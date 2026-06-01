# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #bst so were trying to find a node thats smaller than p and bigger than q
        big = q.val if q.val > p.val else p.val
        small = p.val if p.val < q.val else q.val

        if not root or not p or not q:
            return None

        if root.val < small:
            return self.lowestCommonAncestor(root.right, p, q)
        elif root.val > big:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return root
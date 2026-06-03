# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        '''
        Go down and check the max path if we split at this node
        then return the max path if we didnt split here to the parent
        '''
        res = [root.val]

        def dfs(root: Optional[TreeNode]) -> int:
            if not root:
                return 0
            
            leftMax = max(dfs(root.left), 0)
            rightMax = max(dfs(root.right), 0)

            if_we_split_here = root.val + leftMax + rightMax
            if if_we_split_here > res[0]:
                res[0] = if_we_split_here
            
            return root.val + max(leftMax, rightMax)
        
        dfs(root)
        return res[0]


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid]) #everything upto and excluding mid for inorder
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        return root    
            
        #On a high level just think about this:
        '''
        I know the first thing in preorder is my root.
        Now lemme split up my left subtree and right subtree and repeat this base case
        I can split it up into the two subtrees using the two traversal lists
        '''



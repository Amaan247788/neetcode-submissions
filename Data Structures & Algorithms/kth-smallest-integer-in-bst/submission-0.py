# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # brute force - do a in order traversal and store every node in a container then return k-1 index
        def inOrderTraversal(root, nodes: List[int]) -> None:
            if not root:
                return
            
            inOrderTraversal(root.left, nodes)
            nodes.append(root.val)
            inOrderTraversal(root.right, nodes)
        
        nodes = []
        inOrderTraversal(root, nodes)

        return nodes[k-1]


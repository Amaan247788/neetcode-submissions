"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import defaultdict
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = defaultdict(Node)
        
        def dfs(node:Optional['Node']) -> None:
            
            if node.val in oldToNew:
                return oldToNew[node.val]
            
            newNode = Node(node.val)
            oldToNew[node.val] = newNode
            for neighbor in node.neighbors:
                newNode.neighbors.append(dfs(neighbor))
            return newNode
        
        if not node:
            return None
        
        return dfs(node)
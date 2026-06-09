from collections import defaultdict
class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.end = False
        self.word = None
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        for word in words:
            curr = root
            for c in word:
                if c not in curr.children:
                    curr.children[c] = TrieNode()
                curr = curr.children[c]
            curr.word = word
        
        xMax = len(board)
        yMax = len(board[0])
        ans = []
        
        def dfs(x: int, y: int, node: TrieNode):
            if x >= xMax or x < 0 or y >= yMax or y < 0:
                return
            
            char = board[x][y]
            if char not in node.children or char == '#':
                return
            
            next_node = node.children[char]

            if next_node.word:
                ans.append(next_node.word)
                next_node.word = None  
            
            board[x][y] = '#'
            
            dfs(x+1,y,next_node)
            dfs(x-1,y,next_node)
            dfs(x,y+1,next_node)
            dfs(x,y-1,next_node)

            board[x][y] = char
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(i, j, root)
        return ans
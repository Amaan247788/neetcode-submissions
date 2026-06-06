class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        #just do a dfs when you find the first char of word
        n = len(word)
        def dfs(x: int, y:int, i:int) -> bool:
            # i is the index of the char were currently looking for
            if i == n:
                return True
            if x >= len(board) or x < 0 or y >= len(board[0]) or y < 0 or word[i] != board[x][y] or board[x][y] == '#':
                return False
            board[x][y] = '#'
            res = dfs(x-1, y, i+1) or dfs(x, y+1, i+1) or dfs(x, y-1, i+1) or dfs(x+1, y, i+1)
            board[x][y] = word[i]
            return res
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    return True
        return False


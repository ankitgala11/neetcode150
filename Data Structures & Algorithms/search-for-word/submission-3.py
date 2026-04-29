class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)
        m = len(board[0])
        x = [1,-1, 0, 0]
        y = [0,0,1,-1]

        vis = [[0]*m for _ in range(n)]


        def issafe(x, y, idx):
            if x>=n or x<0 or y>=m or y<0 or board[x][y] != word[idx] or vis[x][y] == 1:
                return False
            
            return True

        def solve(i, j, idx):
            if idx == len(word):
                return True
            vis[i][j] = 1

            for l in range(4):
                newi = i + x[l]
                newj = j + y[l]

                if issafe(newi, newj, idx):
                    if solve(newi, newj, idx + 1):
                        return True
            vis[i][j] = 0

  
        for i in range(n):
            for j in range(m):

                if board[i][j] == word[0]:
                    if solve(i, j, 1):
                        return True

            
        return False


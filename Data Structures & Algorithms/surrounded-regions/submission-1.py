class Solution:
    def solve(self, board: List[List[str]]) -> None:
        n = len(board)
        m = len(board[0])

        d = [(1,0) ,(-1,0), (0,1), (0,-1)]
        q = []
        for i in range(n):
            if board[i][0] == "O":
                board[i][0]='-'
                q.append((i, 0))
            if board[i][m-1] == "O":
                board[i][m-1]='-'
                q.append((i, m-1))
            
        for j in range(m):
            if board[0][j] == "O":
                board[0][j]='-'
                q.append((0, j))
            if board[n-1][j] == "O":
                board[n-1][j]='-'
                q.append((n-1, j))
            
        while q:
            i, j = q.pop(0)

            for dx, dy in d:
                newi = i+dx
                newj = j+dy

                if newi<n and newi>=0 and newj<m and newj>=0 and board[newi][newj] == "O":
                    board[newi][newj] = '-'
                    q.append((newi, newj))
            

        for i in range(n):
            for j in range(m):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "-":
                    board[i][j] = "O"
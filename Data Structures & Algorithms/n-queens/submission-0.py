class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        board = [['.']*n for _ in range(n)]
        print(board)
        row = {}
        updiag = {}
        downdiag = {}

        def issafe(r, c):
            if r in row and row[r] == 1 or r+c in downdiag and downdiag[r+c] ==1 or c-r in updiag and updiag[c-r] == 1:
                return False
            
            return True



        def solve(c):
            if c>= n:
                temp = []
                for x in board:
                    temp.append(''.join(x))
                res.append(temp[:])
                return

            for r in range(n):
                if issafe(r, c):
                    board[r][c] = 'Q'
                    row[r]=1
                    downdiag[r+c] = 1
                    updiag[c-r] = 1
                    solve(c+1)
                    board[r][c] = '.'
                    row[r]=0
                    downdiag[r+c] = 0
                    updiag[c-r] = 0



        ans , res= [], []
        solve(0)
        return res

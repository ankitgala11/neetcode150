class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        n = len(matrix)
        m = len(matrix[0])

        for i in range(n):
            for j in range(m):

                if matrix[i][j]==0:

                    for c in range(m):
                        if matrix[i][c] != 0:
                            matrix[i][c] = -1

                    for r in range(n):
                        if matrix[r][j] != 0:
                            matrix[r][j] = -1

        for i in range(n):
            for j in range(m):
                if matrix[i][j]==-1:
                    matrix[i][j]=0
        


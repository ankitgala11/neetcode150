class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        n = len(grid)
        m = len(grid[0])
        x = [0 , 0, 1, -1]
        y = [1, -1, 0, 0]

        q = []
        max_mins=0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.append((i,j,0))

        def isSafe(i, j):
            if i<0 or i>=n or j<0 or j>=m or grid[i][j] != 1:
                return False
            
            return True

        while q:
            i, j, mins = q.pop(0)
            max_mins=max(mins, max_mins)

            for p in range(4):
                newi = x[p] + i
                newj = y[p] + j

                if isSafe(newi, newj):
                    grid[newi][newj] = 2
                    q.append((newi, newj, mins+1))


        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return -1
                    
        return max_mins

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        

        q = []
        n = len(grid)
        m = len(grid[0])

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    q.append((i, j, 0))

        def isSafe(i, j):
            if i>=n or i<0 or j>=m or j<0 or grid[i][j] != 2147483647:
                return False
            
            return True
        
        while q:
            i , j, dist = q.pop(0)

            newi=i+1
            newj=j
            if isSafe(newi, newj):
                grid[newi][newj] = dist+1
                q.append((newi, newj, dist+1))

            newi=i-1
            newj=j
            if isSafe(newi, newj):
                grid[newi][newj] = dist+1
                q.append((newi, newj, dist+1))

            newi=i
            newj=j+1
            if isSafe(newi, newj):
                grid[newi][newj] = dist+1
                q.append((newi, newj, dist+1))

            newi=i
            newj=j-1
            if isSafe(newi, newj):
                grid[newi][newj] = dist+1
                q.append((newi, newj, dist+1))
            


        
  
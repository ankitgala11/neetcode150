class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        n = len(heights)
        m = len(heights[0])

        vis1 = [[0]*m for _ in range(n)]
        vis2 = [[0]*m for _ in range(n)]
        x = [1,-1,0,0]
        y = [0, 0,1,-1]

    
        def dfs_pacific(q):
            
            while q:
                i, j = q.pop(0)
                vis1[i][j] = 1

                for p in range(4):
                    newi = i+x[p]
                    newj = j+y[p]

                    if newi>=0 and newi<n and newj>=0 and newj<m and vis1[newi][newj] ==0 and heights[newi][newj]>=heights[i][j]:
                        q.append((newi, newj))


        def dfs_atlantic(q):
            while q:
                i, j = q.pop(0)
                vis2[i][j] = 1

                for p in range(4):
                    newi = i+x[p]
                    newj = j+y[p]

                    if newi>=0 and newi<n and newj>=0 and newj<m and vis2[newi][newj] ==0 and heights[newi][newj]>=heights[i][j]:
                        q.append((newi, newj))

            

    
        ans = []
        q = []
        for i in range(n):
            q.append((i,0))
        for j in range(m):
            q.append((0,j))
        
        dfs_pacific(q)
    
        q = []
        for i in range(n):
            q.append((i,m-1))
        for j in range(m):
            q.append((n-1,j))
        
        dfs_atlantic(q)

        for i in range(n):
            for j in range(m):
                if vis1[i][j] and vis2[i][j]:
                    ans.append([i, j])
    


        
                
 
        
        return ans


            
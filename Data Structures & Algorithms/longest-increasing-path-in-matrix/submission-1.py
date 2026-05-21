class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])

        dp=[[-1]*m for _ in range(n)]
        d=[(1,0), (-1,0), (0,1), (0,-1)]

        

        def solve(i, j):
            if dp[i][j]!=-1:
                return dp[i][j] 
            temp = 1
            for dx, dy in d:
                newi = i+dx
                newj = j+dy


                if newi>=0 and newi<n and newj>=0 and newj<m and matrix[newi][newj]>matrix[i][j]:
                    temp = max(temp , 1 + solve(newi, newj))
                
            
            dp[i][j]= temp
            return dp[i][j]
        
        ans = 1
        for i in range(n):
            for j in range(m):
                ans = max(ans,  solve(i, j))
        
        return ans
            

        # q=[]
        # for i in range(n):
        #     for j in range(m):
        #         if matrix[i][j]>maxi:
        #             maxi = matrix[i][j]
        #             q=[(matrix[i][j], i, j)]
        #         elif matrix[i][j]==maxi:
        #             q.append((matrix[i][j], i, j))
        
        # while q:
        #     val, i, j =q.pop(0)
            # for dx, dy in d:
            #     newi = i+dx
            #     newj = j+dy

            #     if newi>=0 and newi<n and newj>=0 and newj<m and matrix[newi][newj]<val:
            #         dp[newi][newj]=dp[i][j] + 1
            #         ans = max(ans,dp[newi][newj])
            #         q.append((matrix[newi][newj], newi, newj))
        # print(dp)

        # return ans


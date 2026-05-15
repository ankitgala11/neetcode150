class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        heap = []
        heapq.heappush(heap, (grid[0][0], 0, 0))
        d = [(1,0),(-1,0), (0,1), (0,-1)]
        vis = {(0,0)}


        ans = 0
        while heap:
            lvl, i , j = heapq.heappop(heap)
            ans = max(ans, lvl)

            if i==n-1 and j==n-1:
                return ans
            
            for dx , dy in d:
                newi = i + dx
                newj = j + dy

                if newi>=0 and newj>=0 and newi<n and newj<n and (newi, newj) not in vis:
                    heapq.heappush(heap, (grid[newi][newj], newi, newj))
                    vis.add((newi, newj))
                

        return ans
        
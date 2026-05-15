class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        dist = [float('inf')]*n

        dist[src] = 0

        adj = defaultdict(list)

        for u,v,w in flights:
            adj[u].append((v,w))

        ans = float('inf')
        def dfs(i, cost, stop):
            nonlocal ans
            if stop>k:
                return 
            
            if cost>ans:
                return 

            if i == dst:
                ans = min(ans, cost)
                return

            vis.add(i)

            for nbr, wt in adj[i]:
                if nbr not in vis:
                    dfs(nbr, cost + wt, stop+1)

            vis.remove(i)
            return ans

        vis = set()
        dfs(src,0, -1)
        return ans if ans!=float('inf') else -1

        # q = [(src, -1)]

        # while q:
            
        #     i, stop = q.pop(0)
        #     print(dist, i, stop)
        #     if stop>=k:
        #         continue

        #     for nbr, cost in adj[i]:
        #         if dist[nbr]>dist[i]+cost and stop+1<=k:
        #             dist[nbr] = dist[i]+cost
        #             q.append((nbr, stop+1))

        # if dist[dst]!=float('inf'):
        #     return dist[dst]
        
        # return ans



        

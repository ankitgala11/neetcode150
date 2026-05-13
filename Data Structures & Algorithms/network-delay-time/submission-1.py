import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        adj = defaultdict(list)

        for u,v,t in times:
            adj[u].append((v,t))


        heap = []
        heapq.heappush(heap, (0,k))
        vis = [0]*(n+1)
        ans = 0
        

        while heap:
            # print(heap)
            t1, node = heapq.heappop(heap)
            if vis[node] == 1:continue
            vis[node] = 1
            ans = t1

            for nbr, t2 in adj[node]:
                if vis[nbr]==0:
                    heapq.heappush(heap, (t1+t2,nbr))

        for i in range(1, n+1):
            if vis[i] == 0:
                return -1
        return ans

        
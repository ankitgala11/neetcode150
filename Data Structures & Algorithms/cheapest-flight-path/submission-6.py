class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:

        adj = defaultdict(list)

        dist = [float('inf')]*n
        dist[src] = 0

        for u, v, w in flights:
            adj[u].append((v, w))
        
        minh = []
        heapq.heappush(minh, (0, 0, src))

        while minh:
            stop, cost, node = heapq.heappop(minh)

            if stop>k :
                continue
            
            for nbr, w in adj[node]:

                if dist[nbr]>cost+w:
                    dist[nbr]=cost+w
                    heapq.heappush(minh, (stop+1, dist[nbr], nbr))
        

        if dist[dst]!=float('inf'):
            return dist[dst]
        return -1

                    


            



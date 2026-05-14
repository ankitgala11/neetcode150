class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        adj = defaultdict(list)
        edges = []
        n = len(points)

        for i in range(n):
            for j in range(i+1, n):

                dist = abs(points[j][0] - points[i][0]) + abs(points[j][1] - points[i][1])

                edges.append( [dist, i , j  ])
        edges.sort()
        
        parent = [i for i in range(n) ]
        rank = [0]*n
        ans = 0

        def find(node):
            if node == parent[node]:
                return node
            parent[node] = find(parent[node])
            return parent[node]



        def dsu(dist , u, v):
            nonlocal ans
            pu = find(u)
            pv = find(v)

            if pu!=pv:
                ans += dist

                if rank[pu]>rank[pv]:
                    pu, pv = pv, pu
                parent[pv] = pu
                rank[pv] += rank[pu]



        for w, u, v in edges:
            dsu(w, u, v)

        return ans
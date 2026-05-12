class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        adj = defaultdict(list)

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        count = 0
        vis = set()

        def dfs(i):
            vis.add(i)

            for nbr in adj[i]:
                if nbr not in vis:
                    dfs(nbr)

        for i in range(n):
            if i not in vis:
                count += 1
                dfs(i)

        
        return count
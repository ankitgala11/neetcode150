class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        adj = defaultdict(list)

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        vis = [0]*n

        def dfs(i, par):
            vis[i]=1

            for nbr in adj[i]:
                if nbr == par:
                    continue
                if vis[nbr] == 1:
                    return True
                if dfs(nbr, i):
                    return True

            return False


        if dfs(0, -1):
            return False
                
        for i in vis:
            if i == 0: 
                return False
            

        return True
            

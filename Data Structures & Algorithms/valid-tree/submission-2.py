class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        adj = defaultdict(list)

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        vis = [0]*n

        def dfs(i, path, par):
            vis[i]=1
            # print(i, vis)
            path.add(i)

            for nbr in adj[i]:
                if nbr == par:
                    continue
                if nbr in path:
                    return False
                if vis[nbr]!=1:
                    if not dfs(nbr, path, i):
                        return False

                
            path.remove(i)
            return True


        if not dfs(0, set(), -1):
            return False
                
        for i in vis:
            if i == 0: 
                return False
            

        return True
            

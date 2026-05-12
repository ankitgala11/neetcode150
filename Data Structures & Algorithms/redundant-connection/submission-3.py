class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        adj = defaultdict(list)

        def check_cyle(i, path, vis, par):
            vis.add(i)
            path.add(i)

            for nbr in adj[i]:
                if nbr == par:
                    continue
                
                if nbr in path:
                    return True
                
                if nbr not in vis:
                    if check_cyle(nbr, path, vis, i):
                        return True
            path.remove(i)
            return False

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

            if check_cyle(u, set(), set(), -1):
                return [u, v]

            
  
  
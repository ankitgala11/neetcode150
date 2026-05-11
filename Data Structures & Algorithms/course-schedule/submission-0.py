class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)

        for u,v in prerequisites:
            adj[u].append(v)

        vis=set()

        def dfs(i, path):
            vis.add(i)
            path.add(i)

            for nbr in adj[i]:
                if nbr in path:
                    return True
                if nbr not in vis:
                    return dfs(nbr, path)
                
            path.remove(i)
            
        
        for i in range(numCourses):
            if i not in vis:
                if dfs(i, set()):
                    return False
        return True
        

        

        

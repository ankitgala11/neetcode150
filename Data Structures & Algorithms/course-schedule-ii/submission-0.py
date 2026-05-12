class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        adj = defaultdict(list)
        indegree = [0]*numCourses

        for u, v in prerequisites:
            adj[v].append(u)
            indegree[u] += 1

        q = []
        ans = []

        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        while q:
            node = q.pop(0)
            ans.append(node)

            for nbr in adj[node]:
                indegree[nbr] -= 1
                if indegree[nbr] == 0:
                    q.append(nbr)
            
        
        if len(ans) == numCourses:
            return ans
        return []

        
        


        

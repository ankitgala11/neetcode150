class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        ans = []

        for u, v in prerequisites:
            adj[v].append(u)

        vis = set()

        def dfs(node, path):

            vis.add(node)
            path.add(node)
            

            for nbr in adj[node]:

                if nbr in path:
                    return True

                if nbr not in vis:
                    if dfs(nbr, path):
                        return True

            ans.append(node)
            path.remove(node)
            return False


        for i in range(numCourses):

            if i not in vis:
                if dfs(i, set()):
                    return []

        return ans[::-1]
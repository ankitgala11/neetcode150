class Solution:
    def canFinish(self, numCourses, prerequisites):

        adj = defaultdict(list)

        for u, v in prerequisites:
            adj[u].append(v)

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

            path.remove(node)
            return False


        for i in range(numCourses):

            if i not in vis:
                if dfs(i, set()):
                    return False

        return True
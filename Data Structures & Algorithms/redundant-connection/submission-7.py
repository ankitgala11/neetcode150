class Solution:
    def findRedundantConnection(self, edges):

        n = len(edges)

        adj = [[] for _ in range(n + 1)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        vis = set()
        cycle = set()
        cycleStart = [-1]

        def dfs(node, path, par):

            vis.add(node)
            path.add(node)

            for nbr in adj[node]:

                if nbr == par:
                    continue

                if nbr in path:
                    cycleStart[0] = nbr
                    cycle.add(nbr)
                    cycle.add(node)
                    return True

                if nbr not in vis:

                    if dfs(nbr, path, node):

                        if cycleStart[0] != -1:
                            cycle.add(node)

                        if node == cycleStart[0]:
                            cycleStart[0] = -1

                        return True

            path.remove(node)
            return False


        for i in range(1, n + 1):

            if i not in vis:

                if dfs(i, set(), -1):

                    for u, v in edges[::-1]:

                        if u in cycle and v in cycle:
                            return [u, v]

        return []

        # n = len(edges)
        # indegree = [0] * (n + 1)
        # adj = [[] for _ in range(n + 1)]
        # for u, v in edges:
        #     adj[u].append(v)
        #     adj[v].append(u)
        #     indegree[u] += 1
        #     indegree[v] += 1

        # q = deque()
        # print(indegree)
        # for i in range(1, n + 1):
        #     if indegree[i] == 1:
        #         q.append(i)

        # while q:
        #     node = q.popleft()
        #     indegree[node] -= 1
        #     for nei in adj[node]:
        #         indegree[nei] -= 1
        #         if indegree[nei] == 1:
        #             q.append(nei)

        # for u, v in reversed(edges):
        #     if indegree[u]>0 and indegree[v]>0:
        #         return [u, v]
        # return []
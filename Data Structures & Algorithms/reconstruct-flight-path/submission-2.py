from sortedcontainers import SortedList

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(SortedList)

        for u, v in tickets:
            adj[u].add(v)
        

        def dfs(i):
            
            while adj[i]:
                nbr=adj[i][0]
                adj[i].remove(nbr)
                dfs(nbr)
            ans.append(i)

        ans = []
        vis = set()

        dfs("JFK")

        return ans[::-1]

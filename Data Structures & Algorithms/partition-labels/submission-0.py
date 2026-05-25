class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        c = Counter(s)
        n = len(s)
        ans = []

        l=0
        q = set()
        for r in range(n):
            c[s[r]]-=1
            q.add(s[r])
            if c[s[r]] == 0:
                q.remove(s[r])
                if not q:
                    ans.append(r-l+1)
                    l=r+1
            
    
        return ans



        
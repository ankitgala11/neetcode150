class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        
        n = len(words)
        adj = defaultdict(list)
        indegree = [-1]*26
        for word in words:
            for i in word:
                indegree[ord(i)-97]=0

        for i in range(1,n):
            ele1 = words[i-1]
            n1 = len(ele1)
            ele2 = words[i]
            n2=len(ele2)
            if n1 > n2 and ele1[:n2] == ele2:
                return ""

            for j in range(n1):
                if ele1[j] != ele2[j]:
                    adj[ele1[j]].append(ele2[j])

                    indegree[ ord(ele2[j]) - 97] += 1

                    
                    break
        q = []
        for i, v in enumerate(indegree):
            if v == 0:
                q.append(i)

        ans = []

        while q:
            val = q.pop(0)
            ch = chr(val+97)

            ans.append(ch)

            for nbr in adj[ch]:
                indegree[ord(nbr)-97]-=1
                if indegree[ord(nbr)-97] == 0:
                    q.append(ord(nbr)-97)
            

        for i in indegree:
            if i!=0 and i!=-1:

                return ""
        return "".join(ans)


                
            



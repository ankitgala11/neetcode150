class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = defaultdict(list)

        n = len(words)
        
        indegree = [-1]*26
        for i in words:
            for j in i:
                indegree[ord(j)-97]=0
        cnt = 0
        for i in indegree:
            if i == 0:
                cnt += 1
        for i in range(n-1):
            word1 = words[i]
            n1 = len(word1)
            word2 = words[i+1]
            n2 = len(word2)
            l = min(n1,n2)
            j = 0
            while j<l and word1[j]==word2[j]:
                j+=1
            if j==l and len(word1) > len(word2):
                return ""
            if j!= l:
                adj[word1[j]].append(word2[j])

                idx1 = ord(word1[j])-ord('a')
                idx2 = ord(word2[j])-ord('a')
                indegree[idx2] += 1

        ans = []
        q = []
        for i in range(26):
            if indegree[i] == 0:
                q.append(i)

        while q:
            idx = q.pop(0)
            ch = chr(idx + 97)
            ans.append(ch)

            for nbr in adj[ch]:
                
                indegree[ord(nbr)-ord('a')] -= 1
                if indegree[ord(nbr)-ord('a')] == 0:
                    q.append(ord(nbr)-ord('a'))

        if len(ans) != cnt:
            return ""
        return "".join(ans)




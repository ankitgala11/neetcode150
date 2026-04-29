class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
       
        ans = 0
        cnt = 0
        n = len(s)

        for i in range(n):
            mp = {}
            maxf = 0

            for j in range(i, n):
                mp[s[j]] = mp.get(s[j], 0) + 1
                maxf = max(maxf , mp[s[j]])
                if j-i+1 - maxf <= k:
                    ans = max(ans, j-i+1)
                

        return ans



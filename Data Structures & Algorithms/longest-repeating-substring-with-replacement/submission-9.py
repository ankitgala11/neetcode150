class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
       
        ans = 0
        n = len(s)
        j = 0
        mp = {}
        maxi=""
        maxicnt = 0

        for i in range(n):
            mp[s[i]] = mp.get(s[i], 0) + 1
            if mp[s[i]] > maxicnt:
                maxicnt = mp[s[i]]
                maxi = s[i]
                
            if (i - j + 1) - maxicnt <= k:
                ans = max(ans, i - j + 1)
            else:
                while (i - j + 1) - maxicnt > k:
                    mp[s[j]] -= 1
                    maxicnt = max(mp.values())
                    j+=1
                

        return ans

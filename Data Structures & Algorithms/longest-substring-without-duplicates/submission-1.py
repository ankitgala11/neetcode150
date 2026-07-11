class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
       
        n = len(s)
        ans = 0
        mp = {}
        j = 0

        for i in range(n):
            mp[s[i]] = mp.get(s[i], 0) + 1
            if mp[s[i]]==1:
                ans= max(ans, i-j+1)
            else:
                while j<i and mp[s[i]]!=1:
                    mp[s[j]]-=1
                    j+=1
                ans= max(ans, i-j+1)
            
        return ans
                









        
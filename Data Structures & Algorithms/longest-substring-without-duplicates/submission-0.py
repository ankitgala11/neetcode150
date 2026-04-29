class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        seen = {}
        n = len(s)
        j = 0

        for i in range(n):
            if s[i] not in seen or seen[s[i]] == 0:
                ans = max(ans, i-j+1)
                seen[s[i]] = 1
            
            else:
                seen[s[i]] += 1
                while j<=i and seen[s[i]] != 1:
                    seen[s[j]]-=1
                    j+=1
                ans = max(ans, i-j+1)

        
        return ans
                


                




        
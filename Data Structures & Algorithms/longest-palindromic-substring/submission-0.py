class Solution:
    def longestPalindrome(self, s: str) -> str:
        cnt = 1
        ans = s[0]

        n = len(s)

        for i in range(n):
            # odd
            j=i-1
            k=i+1

            while j>=0 and k<n and s[j]==s[k]:
                j-=1
                k+=1
            
            if cnt < k-j-1:
                cnt = k-j-1
                ans = s[j+1:k]

            # even
            if i+1<n and s[i] == s[i+1]:
                if cnt < 2:
                    cnt = 2
                    ans = s[i:i+2]
                j=i-1
                k=i+2

                while j>=0 and k<n and s[j]==s[k]:
                    j-=1
                    k+=1
                
                if cnt < k-j-1:
                    cnt = k-j-1
                    ans = s[j+1:k]

        return ans
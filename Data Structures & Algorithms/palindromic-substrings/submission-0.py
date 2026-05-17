class Solution:
    def countSubstrings(self, s: str) -> int:
        
        cnt = 0
        n = len(s)

        for i in range(n):
            # odd
            j=i
            k=i

            while j>=0 and k<n and s[j]==s[k]:
                j-=1
                k+=1
                cnt += 1


            # even
            j=i
            k=i+1

            while j>=0 and k<n and s[j]==s[k]:
                j-=1
                k+=1
                cnt += 1


        return cnt
        

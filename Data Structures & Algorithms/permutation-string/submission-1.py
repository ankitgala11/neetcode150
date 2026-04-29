class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s = [0]*26
        c = [0] * 26
        m = len(s1)
        n = len(s2)
        if m>n:return False
        
        for i in s1:
            s[ord(i)-ord('a')]+=1

        for i in range(m):
            c[ord(s2[i])-ord('a')]+=1
        
        if s == c:return True

        j = 0
        for i in range(m, n):
            c[ord(s2[j])-ord('a')]-=1
            c[ord(s2[i])-ord('a')]+=1
            j+=1
            if s == c:return True
        
        return False





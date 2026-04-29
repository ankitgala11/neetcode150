class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tt = [0]*256
        ss = [0] * 256
        unique = 0
        need = 0
        n = len(s)
        ans=""
        cnt = n
        j= 0

        for i in t:
            if tt[ord(i)] == 0:
                unique += 1
            tt[ord(i)] += 1

        for i in range(n):
            ss[ord(s[i])] += 1
            if ss[ord(s[i])] == tt[ord(s[i])] :
                need += 1

            while need == unique:
                if cnt>=i-j+1:
                    cnt = i-j+1
                    ans = s[j:i+1]
                ss[ord(s[j])] -= 1
                if ss[ord(s[j])] < tt[ord(s[j])]:
                    need -= 1
                j+=1
        
        return ans

                


            
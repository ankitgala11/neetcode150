class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        scount = [0]*26
        tcount = [0]*26

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            scount[ord(s[i]) - ord('a')] += 1
            tcount[ord(t[i]) - ord('a')] += 1
        
        return scount == tcount
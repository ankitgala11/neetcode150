from functools import lru_cache
class Solution:

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordset = set(wordDict)
        @lru_cache()
        def solve(i):
            if i>=n:
                return True
            
            temp = ""
            for idx in range(i, n):
                temp+=s[idx]
                if temp in wordset:
                    if solve(idx+1):
                        return True

            return False


        n = len(s)
        return solve(0)
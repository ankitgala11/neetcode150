from functools import lru_cache
class Solution:

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordset = set(wordDict)
        memo = {}
        # @lru_cache()
        def solve(i):
            if i>=n:
                return True
            if i in memo:
                return memo[i]
            
            temp = ""
            for idx in range(i, n):
                temp+=s[idx]
                if temp in wordset:
                    if solve(idx+1):
                        memo[i] = True
                        return True
            memo[i] = False
            return False


        n = len(s)
        return solve(0)
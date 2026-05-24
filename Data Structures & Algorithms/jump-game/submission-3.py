import sys
sys.setrecursionlimit(10000)
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        n = len(nums)

        def solve(i):
            if i>=n-1:
                return True
            
            if i in dp:
                return dp[i]
            
            for jump in range(1,1+nums[i]):
                if solve(i+jump):
                    return True
            
            dp[i] =  False
            return False

        dp = {}
        return solve(0)
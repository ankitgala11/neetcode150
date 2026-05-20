
class Solution:

    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total & 1:
            return False

        n = len(nums)

        def solve(i, s):
            if i>=n or s<0:
                return False
            
            if s==0:
                return True

            if dp[i][s]==True:
                return dp[i][s]
            
            take = solve(i+1, s-nums[i])
            nottake = solve(i+1, s)

            dp[i][s] =  take or nottake
            return dp[i][s]

        s = total//2
        # dp = [[False]*(s+1) for _ in range(n)]
        # return solve(0, s)

        def solveTab():
            t = total//2
            dp = [[False]*(t+1) for _ in range(n+1)]

            for i in range(n+1):
                dp[i][0]=True

            for i in range(n-1, -1, -1):
                for s in range(t+1):
                    take=False
                    if s-nums[i]>=0:
                        take = dp[i+1][s-nums[i]]
                    nottake = dp[i+1][s]

                    dp[i][s] =  take or nottake

            return dp[0][t]

        return solveTab()
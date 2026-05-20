class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        def solve(i, prev):
            if i>=n:
                return 0
            if dp[i][prev]!=-1:
                return dp[i][prev]
            take = 0
            if prev==-1 or nums[i]>nums[prev]:
                take = 1 + solve(i+1, i)
            nottake = solve(i+1, prev)

            dp[i][prev]= max(take, nottake)
            return dp[i][prev]
            
        dp = [[-1]*(n) for _ in range(n)]
        return solve(0, -1)
class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def solve(i, end, dp):

            if i >= end:
                return 0
            if dp[i]!=-1:
                return dp[i]
            take = nums[i]+solve(i+2, end, dp)
            nottake = solve(i+1, end, dp)

            dp[i]= max(take, nottake)
            return dp[i]

        n = len(nums)
        if n == 1:
            return nums[0]
        dp1 = [-1]*n
        dp2 = [-1]*n
        return max( solve(0, n-1, dp1) , solve(1, n, dp2))
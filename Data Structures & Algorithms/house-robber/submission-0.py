class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def solve(i):

            if i >= n:
                return 0
            if dp[i]!=-1:
                return dp[i]
            take = nums[i]+solve(i+2)
            nottake = solve(i+1)

            dp[i]= max(take, nottake)
            return dp[i]

        n = len(nums)
        dp = [-1]*n
        return solve(0)
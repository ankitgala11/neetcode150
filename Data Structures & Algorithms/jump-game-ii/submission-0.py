class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)

        def solve(i):
            if i>=n-1:
                return 0
            if dp[i]!=-1:
                return dp[i]
            
            ans = n
            for jump in range(1, nums[i]+1):
                ans = min(ans , 1+ solve(i+jump))
            
            dp[i] = ans
            return ans
        
        dp = [-1]*n
        return solve(0)
            

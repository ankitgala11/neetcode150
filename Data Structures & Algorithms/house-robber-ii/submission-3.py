class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)
        if n == 1:
            return nums[0]
        
        # def solve(i, end, dp):

        #     if i >= end:
        #         return 0
        #     if dp[i]!=-1:
        #         return dp[i]
        #     take = nums[i]+solve(i+2, end, dp)
        #     nottake = solve(i+1, end, dp)

        #     dp[i]= max(take, nottake)
        #     return dp[i]

        # dp1 = [-1]*n
        # dp2 = [-1]*n
        # return max( solve(0, n-1, dp1) , solve(1, n, dp2))


        # def solveTab(s, end, dp):
            
        #     for i in range(end-1, s-1, -1):
        #         take = nums[i]+dp[i+2]
        #         nottake = dp[i+1]

        #         dp[i]= max(take, nottake)
            
        #     return dp[s]
        
        # dp1 = [0]*(n+2)
        # dp2 = [0]*(n+2)
        # return max( solveTab(0, n-1, dp1) , solveTab(1, n, dp2))

        def solveTabOpt(s, end):
            next1=0
            next2=0
            curr=0
            for i in range(end-1, s-1, -1):
                take = nums[i]+next2
                nottake = next1

                curr= max(take, nottake)
                next2 = next1
                next1 = curr
            
            return curr
        

        return max( solveTabOpt(0, n-1) , solveTabOpt(1, n))


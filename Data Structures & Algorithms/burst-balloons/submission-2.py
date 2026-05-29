class Solution:
    def maxCoins(self, nums: List[int]) -> int:

        

        nums = [1] + nums + [1]

        # def solve(l, r):

        #     if l>r:
        #         return 0

        #     if (l,r) in dp:
        #         return dp[(l,r)]
        #     maxi = 0
        #     for i in range(l,r+1):
        #         coins = nums[l-1]*nums[i]*nums[r+1]
        #         maxi = max(maxi , coins + solve(l, i-1)+solve(i+1, r))
            
        #     dp[(l,r)]= maxi
        #     return maxi
            


        # dp = {}
        # return solve(1, len(nums)-2)

        def solveTab():
            n = len(nums)
            dp = [[0]*(n+1) for _ in range(n+1)]
            



            for l in range(n-2, 0,-1):
                for r in range(l, n-1):
                    maxi = 0
                    for i in range(l,r+1):
                        coins = nums[l-1]*nums[i]*nums[r+1]
                        maxi = max(maxi , coins + dp[l][i-1]+dp[i+1][r])
            
                    dp[l][r]= maxi
            return dp[1][n-2]
            


        
        return solveTab()

        
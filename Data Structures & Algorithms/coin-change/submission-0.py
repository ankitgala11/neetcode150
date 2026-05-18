class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        def solve(i, s):
            if i>=n or s>amount:
                return float('inf')
            
            if amount==s:
                return 0
            
            if dp[i][s]!=float('inf'):
                return dp[i][s]
            
            take = 1 + solve(i, s+coins[i])
            nottake = solve(i+1, s)
        
            dp[i][s]= min(take, nottake)
            return dp[i][s]




        n = len(coins)
        dp = [[float('inf')]*(amount+1) for _ in range(n)]
        ans = solve(0, 0) 
        if ans!= float('inf'):return ans
        return -1


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        n = len(nums)

        def solve(i, t):
            if i>n :
                return 0
            
            if i==n:
                if t == target:
                    return 1
                return 0
            
        
            if (i, t) in dp:
                return dp[(i, t)]
            

            add = solve(i+1, t+nums[i])
            sub = solve(i+1, t-nums[i])

            dp[(i, t)] = add+sub
            return dp[(i, t)]

        # dp = {}
        # return solve(0, 0)

        def solveTab():
            dp = {}
            dp[(n, target)]=1
            s = sum(nums)

            for i in range(n-1, -1, -1):
                for t in range(s, -s-1, -1):
            
                    add = sub = 0
                    if (i+1, t+nums[i]) in dp:
                        add = dp[(i+1, t+nums[i])]
                    
                    if (i+1, t-nums[i]) in dp:
                        sub = dp[(i+1 ,t-nums[i])]

                    dp[(i, t)] = add+sub

            print(dp)
            return dp[(0, 0)]

        return solveTab()

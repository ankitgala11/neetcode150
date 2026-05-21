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

        dp = {}
        return solve(0, 0)

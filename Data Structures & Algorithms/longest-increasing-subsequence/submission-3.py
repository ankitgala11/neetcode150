import bisect
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
        # return solve(0, -1)

        def solveTabOpt():
            # dp = [[0]*(n+1) for _ in range(n+1)]
            curr = [0]*(n+1)
            next = [0]*(n+1)

            for i in range(n-1,-1,-1):
                for prev in range(n-1, -2, -1):
                    take = 0
                    if prev==-1 or nums[i]>nums[prev]:
                        take = 1 + next[i+1]
                    nottake = next[prev+1]

                    curr[prev+1]= max(take, nottake)
                next = curr[:]


            return curr[0]

        # return solveTabOpt()



        def solveBs():
            ans = []

            for i in nums:
                if not ans or ans[-1]<i:
                    ans.append(i)
                else:
                    idx = bisect.bisect_left(ans, i)
                    ans[idx] = i



            return len(ans)

        
        return solveBs()



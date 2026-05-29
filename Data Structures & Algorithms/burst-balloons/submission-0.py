class Solution:
    def maxCoins(self, nums: List[int]) -> int:

        

        nums = [1] + nums + [1]

        def solve(l, r):

            if l>r:
                return 0

            if (l,r) in dp:
                return dp[(l,r)]
            maxi = 0
            for i in range(l,r+1):
                coins = nums[l-1]*nums[i]*nums[r+1]
                maxi = max(maxi , coins + solve(l, i-1)+solve(i+1, r))
            
            dp[(l,r)]= maxi
            return dp[(l,r)]
            


        dp = {}
        return solve(1, len(nums)-2)

        
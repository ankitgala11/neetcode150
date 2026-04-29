class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []


        def solve(i):

            if i>=n:
                ans.append(nums[:])
                return
            
            for idx in range(i, n):
                nums[i], nums[idx] = nums[idx] , nums[i]
                solve(i+1)
                nums[i], nums[idx] = nums[idx] , nums[i]

        solve(0)
        return ans
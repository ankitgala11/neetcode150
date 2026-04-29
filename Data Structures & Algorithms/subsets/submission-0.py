class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n= len(nums)
        ans = []

        def solve(i, op):
            if i >= n:
                ans.append(op[:])
                return

            solve(i+1, op)

            op.append(nums[i])
            solve(i+1, op)
            op.remove(nums[i])


        solve(0, [])
        return ans


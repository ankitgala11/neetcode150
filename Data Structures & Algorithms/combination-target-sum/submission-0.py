class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans  = []
        n = len(nums)

        def solve(i, op, s):
            if s == target:
                ans.append(op[:])
                return

            if i >= n or s>target:
                return 
            
            solve(i+1, op, s)
            op.append(nums[i])
            solve(i, op, s+nums[i])
            op.pop()
        
        solve(0 , [], 0)
        return ans

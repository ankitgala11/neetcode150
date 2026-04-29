class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        n = len(nums)
        nums.sort()
        ans = set()

        def solve(i, op):

            if i >= n:
                ans.add(tuple(op))
                return

            solve(i+1, op)
            op.append(nums[i])
            solve(i+1, op)
            op.pop()

        
        solve(0, [])

        res = [list(i) for i in ans]
        return res
            

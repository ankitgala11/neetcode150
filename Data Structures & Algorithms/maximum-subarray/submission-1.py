class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        curr = float('-inf')
        ans = float('-inf')

        for i in nums:
            curr = max(curr+i, i)
            ans = max(ans, curr)
        
        return ans
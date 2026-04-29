class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        if len(s) == 0:return 0
        ans = 1
        res = 1

        for i in nums:
            if i-1 not in s:

                j = i
                while j+1 in s:
                    ans+=1 
                    j += 1
                res = max(res, ans)
                ans = 1
        
        return res
                


        
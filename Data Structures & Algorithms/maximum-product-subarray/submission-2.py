class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        pre=1
        suff=1
        n = len(nums)
        ans=float('-inf')
        
        for i in range(n):
            
            if pre==0:pre=1
            if suff==0:suff=1
            
            pre*=nums[i]
            suff*=nums[n-1-i]
            
            ans=max(ans, pre, suff)
            
            
    
        return ans
        # curr_max = curr_min = res = nums[0]
        # for num in nums[1:]:
        #     temp_max = max(num, curr_max * num, curr_min * num)
        #     temp_min = min(num, curr_max * num, curr_min * num)
        #     curr_max, curr_min = temp_max, temp_min
        #     res = max(res, curr_max)
        # return res
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr_max = curr_min = res = nums[0]
        for num in nums[1:]:
            temp_max = max(num, curr_max * num, curr_min * num)
            temp_min = min(num, curr_max * num, curr_min * num)
            curr_max, curr_min = temp_max, temp_min
            res = max(res, curr_max)
        return res
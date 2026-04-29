class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}
        n = len(nums)

        for i in range(n):
            if target - nums[i] in mp:
                return sorted([mp[target - nums[i]], i])

            mp[nums[i]] = i

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        suffix = [1]

        n = len(nums)

        for i in range(n-1):
            prefix.append(prefix[-1] * nums[i])
            suffix.append(suffix[-1] * nums[n-1-i])

        suffix = suffix[::-1]

        ans = [0] * n
        for i in range(n):
            ans[i] = prefix[i] * suffix[i]

        return ans


        



        
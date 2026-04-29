class Solution:
    def findMin(self, nums: List[int]) -> int:

        s = 0
        e = len(nums) - 1

        if nums[0]<=nums[-1]:
            return nums[0]

        ans = 0


        while s<=e:
            m = (s+e)//2

            if nums[m]<nums[0]:
                ans = nums[m]
                e = m-1
            
            else:
                s = m +1

        
        return ans
        
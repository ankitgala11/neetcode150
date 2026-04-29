class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        n = len(nums)
        q = []
        
        for i in range(k):
            while q and nums[q[-1]]<nums[i]:
                q.pop()
            q.append(i)

        ans.append(nums[q[0]])

        for i in range(k, n):
            while q and q[0]<=i-k:
                q.pop(0)
            while q and nums[q[-1]]<nums[i]:
                q.pop()
            q.append(i)
            ans.append(nums[q[0]])
    
        return ans

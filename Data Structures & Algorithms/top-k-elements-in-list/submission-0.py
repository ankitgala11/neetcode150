class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)


        ans = sorted(count, key = lambda x : -count[x])

       
        return ans[:k]


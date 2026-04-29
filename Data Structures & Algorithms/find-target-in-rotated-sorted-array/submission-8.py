class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def pivot():
            s = 0
            e = len(nums)-1
            ans = 0
            while s<=e:
                m = (s+e)//2

                if nums[m]<nums[0]:
                    ans = m
                    e = m - 1
                
                else:
                    s = m+1
                
            return ans

        def search(s, e):

            while s<=e:
                m = (s+e)//2

                if nums[m]==target:
                    return m
                elif nums[m]>target:
                    e = m - 1
                else:
                    s = m+1
            
            return -1
                
        p = pivot()

        if p!=0 and target <= nums[p-1] and target>=nums[0]:
            return search(0,p-1)
        else:
            return search(p, len(nums)-1)

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        n1 = len(nums1)
        n2 = len(nums2)

        if n2<n1:
            return self.findMedianSortedArrays(nums2, nums1)

        total = n1+n2

        median = (total+1)//2

       
        low = 0
        high = n1
        

        while low <= high:
            m1 = (low+high)//2
            m2 = median - m1


            l1,l2=float('-inf'),float('-inf')
            if m1:
                l1=nums1[m1-1]
            if m2:
                l2=nums2[m2-1]

            
            r1 = nums1[m1] if m1<n1 else float('inf')
            r2 = nums2[m2] if m2<n2 else float('inf')

            if l1<=r2 and l2<=r1:
                if total & 1:
                    return max(l1, l2)
                
                else:
                    return (max(l1,l2) + min(r1,r2)) / 2

            
            elif l1>r2:
                high = m1-1



            elif l2>r1:
                low = m1 + 1






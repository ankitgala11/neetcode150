class Solution:
    def reverse(self, x: int) -> int:
        l = -pow(2, 31)
        h = pow(2,31)-1

        rev = str(x)
        if rev[0]=='-':
            temp = str(rev[1:])
            ans = int(temp[::-1])*(-1)
        else:
            ans = int(rev[::-1])
        
        if l<=ans<=h:
            return ans
        return 0
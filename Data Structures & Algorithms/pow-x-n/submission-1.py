class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n==0:return 1
        if x == 0:return 0
        if n<0:
            x = 1/x
        ans=x
        n = abs(n)

        for i in range(n-1):
            ans*=x
            
        
        return ans
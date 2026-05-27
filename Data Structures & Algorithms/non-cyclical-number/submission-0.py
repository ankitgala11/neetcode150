class Solution:
    def isHappy(self, n: int) -> bool:
        
        def solve(i):
            temp = [int(num)*int(num) for num in list(str(i))]
            s = sum(temp)
            if s == 1:
                return True
            
            if s in memo:
                return False
            
            memo.add(s)
            return solve(s)


        
        memo = set()
        return solve(n)
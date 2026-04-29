class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        ans= []

        def solve(open, close, op):
            if close == n and open==close:
                ans.append(op)
                return
            if close>n or close>open or open>n:
                return
            
            solve(open+1, close, op+'(')
            solve(open, close+1, op+')')

        solve(0, 0, "")
        return ans


        
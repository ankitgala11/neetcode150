class Solution:
    def partition(self, s: str) -> List[List[str]]:

        def pal(word) :
            return word == word[::-1]

        n = len(s)
        ans = []

        def solve(i, op):
            if i >= n:
                ans.append(op[:])
                return

            temp = ""
            for j in range(i, n):
                temp += s[j]
                if pal(temp):
                    op.append(temp)
                    solve(j+1, op)
                    op.pop()


        
        solve(0, [])

        return ans

        
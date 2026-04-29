class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        mp = {2: ['a','b','c'],3: ['d','e','f'],4: ['g','h','i'],5: ['j','k','l'],6: ['m','n','o'],7: ['p','q','r','s'],8: ['t','u','v'],9: ['w','x','y','z']}

        def solve(i, op):
            if i>=len(digits):
                ans.append(op)
                return

            temp = mp[int(digits[i])]

            for j in range(len(temp)):
                solve(i+1, op+temp[j])



        ans = []
        if not digits:return ans
        solve(0, "")

        return ans

            

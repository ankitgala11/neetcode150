class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n

        # for i in range(n-1, -1, -1):
        #     for j in range(i+1, n):

        #         if temperatures[j] > temperatures[i]:
        #             ans[i] = j-i
        #             break

        # return ans

        stack = []
        
        for i in range(n-1, -1, -1):
            if not stack:
                stack.append(i)
            
            else:

                while stack and temperatures[stack[-1]]<=temperatures[i]:
                    stack.pop()

                if stack:
                    ans[i] = stack[-1]-i
                stack.append(i)
                
        
        return ans



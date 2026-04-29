class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        n = len(heights)

        def nextsmall():
            ans = [0] * n
            stack = [-1]

            for i in range(n-1, -1, -1):
                while stack[-1] != -1 and heights[i] <= heights[stack[-1]]:
                    stack.pop()
                
                ans[i] = stack[-1]
                stack.append(i)
                
            return ans

        def prevsmall():
            ans = [0] * n
            stack = [-1]

            for i in range(n):
                while stack[-1] != -1 and heights[i] <= heights[stack[-1]]:
                    stack.pop()
                
                ans[i] = stack[-1]
                stack.append(i)
                
            return ans


        def cal_area():
            prev = prevsmall()
            next = nextsmall()
            # print(prev, next)

            ans = 0
            

            for i in range(n):
                w = heights[i]
                if next[i] == -1:
                    l = n - prev[i] -1
                else:
                    l = next[i]-prev[i]-1
                
                ans = max(ans, w*l)

            return ans



        return cal_area()


        

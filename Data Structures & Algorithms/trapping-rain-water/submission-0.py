class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        prevgreater = [height[0]]
        nextgreater = [height[-1]]

        for i in range(1, n):
            if height[i]>prevgreater[-1]:
                prevgreater.append(height[i])
            else:
                prevgreater.append(prevgreater[-1])
            
            if height[n-1-i]>nextgreater[-1]:
                nextgreater.append(height[n-1-i])
            else:
                nextgreater.append(nextgreater[-1])
            
        nextgreater = nextgreater[::-1]

        ans = 0
        for i in range(n):
            ans += min(prevgreater[i], nextgreater[i])- height[i]

        return ans


            

        
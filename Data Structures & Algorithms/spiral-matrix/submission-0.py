class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        m = len(matrix[0])
        ans = []
        fr = fc = 0
        lr = n-1
        lc = m-1

        total = n * m
        cnt = 0

        while cnt<total:
            for i in range(fc, lc+1):
                if cnt<total:
                    ans.append(matrix[fr][i])
                    cnt+=1
            fr += 1
            for i in range(fr, lr+1):
                if cnt<total:
                    ans.append(matrix[i][lc])
                    cnt+=1
            lc -= 1
  
            for i in range(lc, fc-1, -1):
                if cnt<total:
                    ans.append(matrix[lr][i])
                    cnt+=1
            lr -= 1
            for i in range(lr, fr-1, -1):
                if cnt<total:
                    ans.append(matrix[i][fc])
                    cnt+=1
            fc += 1


        return ans
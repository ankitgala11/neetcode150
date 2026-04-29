class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        n = len(matrix)
        m = len(matrix[0])



        s= 0
        e = n*m-1


        while s<=e:

            mid = (s+e) // 2

            i = mid // m
            j = mid % m

            if matrix[i][j] == target:
                return True
            
            elif matrix[i][j] < target:
                s = mid +1
            
            else:
                e = mid -1

        return False
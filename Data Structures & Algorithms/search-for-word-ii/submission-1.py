class Trie:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        ans = []
        n = len(board)
        m = len(board[0])
        root = Trie()

        def insert(root, word):
            for i in word:
                if i not in root.children:
                    root.children[i] = Trie()
                root=root.children[i]
            root.isEnd=True


        for word in words:
            insert(root, word)


        def solve(r, c, root, op):
            if r<0 or r>= n or c<0 or c>=m or (r,c) in vis or board[r][c] not in root.children:
                return False

            vis.add((r,c))
            op+=board[r][c]
            root=root.children[board[r][c]]
            if root.isEnd:
                ans.add(op)
            
            solve(r+1,c, root, op)
            solve(r-1,c, root, op)
            solve(r,c+1, root, op)
            solve(r,c-1, root, op)

            vis.remove((r,c))
            

        ans= set()
        vis = set()
        for r in range(n):
            for c in range(m):
                solve(r,c,root, "")

        return list(ans)

        # x = [1,-1,0,0]
        # y = [0, 0, 1, -1]

        # def isSafe(i, j, idx, word):
        #     if i<0 or i>= n or j<0 or j>=m or vis[i][j] == 1 or board[i][j] != word[idx]:
        #         return False
        #     return True

        # def solve(i, j, idx, word):
        #     if idx>=len(word):
        #         return True
            
        #     vis[i][j] = 1

        #     for p in range(4):
        #         newi = i + x[p]
        #         newj = j + y[p]

        #         if isSafe(newi, newj, idx, word):
        #             if solve(newi, newj, idx+1, word):
        #                 return True

                    
        #     vis[i][j] = 0
        #     return False


        # for word in words:
        #     flag=False
        #     for i in range(n):
        #         for j in range(m):
        #             if board[i][j] == word[0]:
        #                 vis = [[0]*m for _ in range(n)]
        #                 if solve(i, j, 1, word):
                            
        #                     ans.append(word)
        #                     flag=True
        #                     break
        #         if flag:
        #             break
        
        # return ans



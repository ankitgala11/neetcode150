# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def solve(subroot):
            if not subroot:
                return "#"

            left = solve(subroot.left)
            right = solve(subroot.right)

            return left + "$"+str(subroot.val)+"$"+right

        
        sub = {}
        sub[solve(subRoot)] = 1
        

        def check(root):
            nonlocal sub

            if not root:
                return "#"

            left = check(root.left)
            right = check(root.right)

            temp = left + "$" + str(root.val) + "$" + right


            if temp in sub:
                ans[0] = True

            return temp

        ans = [False]
        check(root)
        print(ans)
        return ans[0]


        




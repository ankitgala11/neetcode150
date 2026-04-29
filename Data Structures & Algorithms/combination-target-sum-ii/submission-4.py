class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        ans = []
        n = len(candidates)

        def solve(i, path, total):

            if total == target:
                ans.append(path[:])
                return

            if i >= n or total > target:
                return


            # PICK current
            path.append(candidates[i])
            solve(i + 1, path, total + candidates[i])
            path.pop()


            # NOT PICK current
            # skip duplicates
            while i + 1 < n and candidates[i] == candidates[i+1]:
                i += 1

            solve(i + 1, path, total)


        solve(0, [], 0)
        return ans
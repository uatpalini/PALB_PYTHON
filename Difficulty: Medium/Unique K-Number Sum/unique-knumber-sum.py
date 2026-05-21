class Solution:
    def combinationSum(self, n, k):
        res = []
        path = []

        def backtrack(start, k, n):

            if k == 0 and n == 0:
                res.append(path[:])
                return

            if k == 0 or n < 0:
                return

            for i in range(start, 10):
                path.append(i)
                backtrack(i + 1, k - 1, n - i)
                path.pop()

        backtrack(1, k, n)
        return res
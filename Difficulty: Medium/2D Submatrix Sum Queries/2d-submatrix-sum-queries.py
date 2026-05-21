class Solution:
    def prefixSum2D(self, a, query):
        n, m = len(a), len(a[0])

        # Build prefix sum
        prefix = [[0] * m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                prefix[i][j] = a[i][j]

                if i > 0:
                    prefix[i][j] += prefix[i - 1][j]
                if j > 0:
                    prefix[i][j] += prefix[i][j - 1]
                if i > 0 and j > 0:
                    prefix[i][j] -= prefix[i - 1][j - 1]

        ans = []

        for r1, c1, r2, c2 in query:
            res = prefix[r2][c2]

            if r1 > 0:
                res -= prefix[r1 - 1][c2]
            if c1 > 0:
                res -= prefix[r2][c1 - 1]
            if r1 > 0 and c1 > 0:
                res += prefix[r1 - 1][c1 - 1]

            ans.append(res)

        return ans
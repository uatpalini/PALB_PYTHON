class Solution:
    def maxPeople(self, arr):
        n = len(arr)

        left_block = [-1] * n
        right_block = [n] * n

        stack = []

        # Left boundary (previous greater or equal)
        for i in range(n):
            while stack and arr[stack[-1]] < arr[i]:
                stack.pop()

            if stack:
                left_block[i] = stack[-1]

            stack.append(i)

        stack = []

        # Right boundary
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] < arr[i]:
                stack.pop()

            if stack:
                right_block[i] = stack[-1]

            stack.append(i)

        ans = 0

        for i in range(n):
            visible = (i - left_block[i]) + (right_block[i] - i) - 1
            ans = max(ans, visible)

        return ans
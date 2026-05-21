class Solution:
    def has132Pattern(self, arr):
        n = len(arr)
        stack = []
        third = float('-inf')

        for i in range(n - 1, -1, -1):

            if arr[i] < third:
                return True

            while stack and stack[-1] < arr[i]:
                third = stack.pop()

            stack.append(arr[i])

        return False
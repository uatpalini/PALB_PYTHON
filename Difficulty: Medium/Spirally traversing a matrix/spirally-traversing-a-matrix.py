class Solution:
    def spirallyTraverse(self, mat):
        
        result = []

        top = 0
        bottom = len(mat) - 1
        left = 0
        right = len(mat[0]) - 1

        while top <= bottom and left <= right:

            # Traverse top row
            for i in range(left, right + 1):
                result.append(mat[top][i])
            top += 1

            # Traverse right column
            for i in range(top, bottom + 1):
                result.append(mat[i][right])
            right -= 1

            # Traverse bottom row
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    result.append(mat[bottom][i])
                bottom -= 1

            # Traverse left column
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    result.append(mat[i][left])
                left += 1

        return result
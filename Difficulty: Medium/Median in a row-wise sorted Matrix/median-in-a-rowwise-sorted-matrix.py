class Solution:
    def median(self, mat):

        arr = []

        # Store all elements in one list
        for row in mat:
            for num in row:
                arr.append(num)

        # Sort the list
        arr.sort()

        # Return middle element
        return arr[len(arr) // 2]
        
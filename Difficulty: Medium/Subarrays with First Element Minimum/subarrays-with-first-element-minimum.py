class Solution:
    def countSubarrays(self, arr):
        n = len(arr)

        st = []
        next_smaller = [n] * n

        # Step 1: Next smaller element to the right
        for i in range(n - 1, -1, -1):

            while st and arr[st[-1]] >= arr[i]:
                st.pop()

            if st:
                next_smaller[i] = st[-1]

            st.append(i)

        # Step 2: count subarrays
        total = 0

        for i in range(n):
            total += (next_smaller[i] - i)

        return total
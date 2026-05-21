class Solution:
    def minSwap(self, arr, k):
        
        # Count elements <= k
        good = 0
        for num in arr:
            if num <= k:
                good += 1

        # Count bad elements in first window
        bad = 0
        for i in range(good):
            if arr[i] > k:
                bad += 1

        ans = bad

        # Sliding window
        i = 0
        j = good

        while j < len(arr):

            if arr[i] > k:
                bad -= 1

            if arr[j] > k:
                bad += 1

            ans = min(ans, bad)

            i += 1
            j += 1

        return ans
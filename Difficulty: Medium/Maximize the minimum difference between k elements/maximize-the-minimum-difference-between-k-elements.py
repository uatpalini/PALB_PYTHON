class Solution:
    def maxMinDiff(self, arr, k):
        arr.sort()

        def can(mid):
            count = 1
            last = arr[0]

            for i in range(1, len(arr)):
                if arr[i] - last >= mid:
                    count += 1
                    last = arr[i]

                if count == k:
                    return True

            return False

        l, r = 0, arr[-1] - arr[0]
        ans = 0

        while l <= r:
            mid = (l + r) // 2

            if can(mid):
                ans = mid
                l = mid + 1
            else:
                r = mid - 1

        return ans
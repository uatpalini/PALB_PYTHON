import heapq

class Solution:
    def minOperations(self, arr):
        total = sum(arr)
        target = total / 2

        # max heap (use negative values)
        heap = [-x for x in arr]
        heapq.heapify(heap)

        operations = 0

        while total > target:
            x = -heapq.heappop(heap)   # largest element

            reduced = x / 2
            total -= (x - reduced)

            heapq.heappush(heap, -reduced)
            operations += 1

        return operations
class Solution:
    def findUnion(self, a, b):
        union_set = set(a) | set(b)
        return list(union_set)
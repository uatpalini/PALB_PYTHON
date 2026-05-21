class Solution:
    def countBalanced(self, arr):
        def is_vowel(c):
            return c in "aeiou"

        n = len(arr)

        prefix = 0
        freq = {0: 1}
        ans = 0

        for s in arr:

            val = 0
            for ch in s:
                if is_vowel(ch):
                    val += 1
                else:
                    val -= 1

            prefix += val

            if prefix in freq:
                ans += freq[prefix]
                freq[prefix] += 1
            else:
                freq[prefix] = 1

        return ans
class Solution:
    def substrWithVowels(self, s1, s2):
        from collections import defaultdict

        need = defaultdict(int)
        for ch in s1:
            need[ch] += 1

        window = defaultdict(int)

        have = 0
        required = len(need)

        l = 0
        ans = float('inf')

        for r in range(len(s2)):
            ch = s2[r]
            window[ch] += 1

            if ch in need and window[ch] == need[ch]:
                have += 1

            while have == required:
                ans = min(ans, r - l + 1)

                left_char = s2[l]
                window[left_char] -= 1

                if left_char in need and window[left_char] < need[left_char]:
                    have -= 1

                l += 1

        return -1 if ans == float('inf') else ans
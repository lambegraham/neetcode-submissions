from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        window = defaultdict(int)

        have = 0
        required = len(need)
        l = 0

        bestLength = float("inf")
        best = [0, 0]

        for r, char in enumerate(s):
            window[char] += 1

            if char in need and window[char] == need[char]:
                have += 1

            while have == required:
                if r - l + 1 < bestLength:
                    bestLength = r - l + 1
                    best = [l, r]

                leftChar = s[l]

                if leftChar in need and window[leftChar] == need[leftChar]:
                    have -= 1

                window[leftChar] -= 1
                l += 1

        return s[best[0] : best[1] + 1] if bestLength != float("inf") else ""
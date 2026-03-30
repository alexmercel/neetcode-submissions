from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l, r = 0, 0
        count = {}
        lt = len(t)
        res = ""

        if not s or not t:
            return ""

        for c in t:
            count[c] = count.get(c, 0) + 1

        minlen = float("inf")

        while r < len(s):
            if count.get(s[r], 0) > 0:
                lt -= 1
            count[s[r]] = count.get(s[r], 0) - 1

            # valid window → shrink
            while lt == 0:
                if r - l + 1 < minlen:
                    minlen = r - l + 1
                    res = s[l:r+1]

                count[s[l]] += 1
                if count[s[l]] > 0:
                    lt += 1
                l += 1

            r += 1

        return res
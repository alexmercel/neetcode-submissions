from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = defaultdict(int)
        l = 0
        maxlen = 0

        for r in range(len(s)):
            while seen[s[r]] > 0:
                seen[s[l]] -= 1
                l += 1

            seen[s[r]] += 1
            maxlen = max(maxlen, r - l + 1)

        return maxlen
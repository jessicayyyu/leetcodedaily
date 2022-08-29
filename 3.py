def lengthOfLongestSubstring(self, s: str) -> int:
    left, res = 0, 0
    seen = {}
    for right in range(len(s)):
        c = s[right]
        if c in seen:
            left = max(left, seen.get(c))
        seen[c] = right + 1 #left, right inclusive so add 1 to right to include it
        res = max(res, right - left + 1)
    return res

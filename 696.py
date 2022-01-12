def countBinarySubstrings(self, s: str) -> int:
    if not s:
        return 0
    res = 0
    left, right = 0, 1
    for i in range(1, len(s)):
        if s[i-1] != s[i]:
            res += min(left, right)
            left, right = right, 1
        else:
            right += 1
    return res + min(left, right)
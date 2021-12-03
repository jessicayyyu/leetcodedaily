def lengthOfLongestSubstring(self, s: str) -> int:
    i, j = 0, 0
    unique_chars = set()
    longest = 0
    n = len(s)
    for i in range(n):
        while j < n and s[j] not in unique_chars:
            unique_chars.add(s[j])
            j += 1
        longest = max(longest, j-i)
        unique_chars.remove(s[i])
    return longest
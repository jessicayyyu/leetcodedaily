def longestPalindrome(self, s: str) -> str:
    self.longest_string = ''
    for mid in range(len(s)):
        self.extend_palindrome(s, mid, mid)
        self.extend_palindrome(s, mid, mid+1)
    return self.longest_string

def extend_palindrome(self, s, lo, hi):
    while lo >= 0 and hi < len(s) and s[lo] == s[hi]:
        lo -= 1
        hi += 1
    lo += 1
    if hi - lo > len(self.longest_string):
        self.longest_string = s[lo:hi]
def reverseWords(self, s: str) -> str:
    l, r = 0, 0
    res = ''
    while r < len(s):
        if s[r] != ' ':
            r += 1
        elif s[r] == ' ':
            res += s[l: r+1][::-1]
            r += 1
            l = r
    res += ' '
    res += s[l:][::-1]
    return res[1:]
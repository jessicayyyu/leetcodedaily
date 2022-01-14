def minFlipsMonoIncr(self, s: str) -> int:
    m, n = 0, 0
    for num in s:
        m += int(num)
        n = min(m, n+1-int(num))
    return n
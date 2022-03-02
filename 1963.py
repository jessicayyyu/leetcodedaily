def minSwaps(self, s: str) -> int:
    right, res = 0, 0
    for c in s:
        if c == ']':
            right += 1
        else:
            right -= 1
        res = max(res, right)
    return  (res + 1) //2
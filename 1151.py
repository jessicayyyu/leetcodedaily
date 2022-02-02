def minSwaps(self, data: List[int]) -> int:
    width, maxWin, cntWin, l = sum(data), 0, 0, -1
    for r, d in enumerate(data):
        cntWin += d
        if r - l > width:
            l += 1
            cntWin -= data[l]
        maxWin = max(maxWin, cntWin)
    return width - maxWin
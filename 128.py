def longestConsecutive(self, nums: List[int]) -> int:
    max_len, table = 0, {num: True for num in nums}
    for lo in nums:
        if lo - 1 not in table:
            hi = lo + 1
            while hi in table:
                hi += 1
            max_len = max(max_len, hi - lo)
    return max_len
def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
    intervals.sort(key = lambda x: (x[0], -x[1]))
    counter, prev_end = 0, 0
    for _, end in intervals:
        if end > prev_end:
            prev_end = end
            counter += 1
    return counter
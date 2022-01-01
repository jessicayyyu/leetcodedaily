def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
    res = []
    removedLeft, removedRight = toBeRemoved
    for left, right in intervals:
        if left > removedRight or right < removedLeft:
            res.append([left, right])
        else:
            if left < removedLeft:
                res.append([left, removedLeft])
            if right > removedRight:
                res.append([removedRight, right])
    return res
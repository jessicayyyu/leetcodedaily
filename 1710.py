def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
    boxTypes.sort(key=lambda x: -x[1])
    res = 0
    for box, unit in boxTypes:
        if truckSize > box:
            truckSize -= box
            res += box*unit
        else:
            res += truckSize*unit
            return res
    return res
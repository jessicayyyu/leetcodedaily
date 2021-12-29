def trap(self, height: List[int]) -> int:
    if not height:
        return 0

    left_max = []
    cur_max = 0
    for h in height:
        cur_max = max(h, cur_max)
        left_max.append(cur_max)

    right_max = []
    cur_max = 0
    for h in reversed(height):
        cur_max = max(cur_max, h)
        right_max.append(cur_max)
    right_max.reverse()

    res = 0
    for i in range(len(height)):
        res += min(left_max[i], right_max[i]) - height[i]
    return res


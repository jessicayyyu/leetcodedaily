import math


def minSubArrayLen(self, target: int, nums: List[int]) -> int:
    total, res = 0, math.inf
    left = 0
    for i in range(len(nums)):
        total += nums[i]
        while total >= target:
            res = min(res, i-left+1)
            total -= nums[left]
            left += 1
    if res == math.inf:
        return 0
    return res
import sys
def maxSubArray(self, nums: List[int]) -> int:
    prefixsum = 0
    minsum, maxsum = 0, -sys.maxsize
    for num in nums:
        prefixsum += num
        maxsum = max(maxsum, prefixsum-minsum)
        minsum = min(minsum, prefixsum)
    return maxsum

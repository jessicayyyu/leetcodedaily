def firstMissingPositive(self, nums: List[int]) -> int:
    n = len(nums)
    complete = {n for n in range(1, n+2)}
    for num in nums:
        if num in complete:
            complete.remove(num)
    return min(complete)
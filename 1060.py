def missingElement(self, nums: List[int], k: int) -> int:
    if not nums or not k:
        return 0
    completelen = nums[-1] - nums[0] + 1
    missing = completelen - len(nums)
    if k > missing:
        return nums[-1] + k - missing
    left, right = 0, len(nums) - 1
    while left + 1 < right:
        mid = (left + right) // 2
        missing = nums[mid] - nums[left] - (mid - left)
        if missing < k:
            left = mid
            k -= missing
        else:
            right = mid
    return nums[left] + k
def nextPermutation(self, nums: List[int]) -> None:
    n = len(nums)
    for i in range(n-2, -1, -1):
        if nums[i] < nums[i+1]:
            break
    else:
        nums.reverse()
        return nums
    for j in range(n-1, i, -1):
        if nums[j] > nums[i]:
            nums[j], nums[i] = nums[i], nums[j]
            break
    left, right = i + 1, n -1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
    return nums

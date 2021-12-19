def findDuplicate(self, nums: List[int]) -> int:
    start, end = 0, len(nums) - 1
    while start + 1 < end:
        mid = (start + end) // 2
        counter = 0
        for num in nums:
            if num <= mid:
                counter += 1
        if counter <= mid:
            start = mid
        else:
            end = mid
    return end

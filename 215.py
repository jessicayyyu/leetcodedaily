def findKthLargest(self, nums: List[int], k: int) -> int:
    if not nums or not k or k > len(nums):
        return None
    return self.partition(nums, 0, len(nums)-1, len(nums)-k)

def partition(self, nums, start, end, k):
    if start == end:
        return nums[k]
    pivot = nums[(start+end)//2]
    left, right = start, end
    while left <= right:
        while left <= right and nums[left] < pivot:
            left += 1
        while left <= right and nums[right] > pivot:
            right -= 1
        if left <= right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
    if k <= right:
        return self.partition(nums, start, right, k)
    if k >= left:
        return self.partition(nums, left, end, k)
    return nums[k]
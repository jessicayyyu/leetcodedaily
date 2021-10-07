def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
    nums = sorted(nums)
    result = []
    self.dfs(nums, 0, [], result)
    return result


def dfs(self, nums, index, subset, result):
    result.append(subset[:])
    for i in range(index, len(nums)):
        if nums[i] == nums[i - 1] and i > index:
            continue
        subset.append(nums[i])
        self.dfs(nums, i + 1, subset, result)
        subset.pop()
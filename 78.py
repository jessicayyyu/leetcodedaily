def subsets(self, nums: List[int]) -> List[List[int]]:
    result = []
    nums = sorted(nums)
    self.dfs(nums, 0, [], result)
    return result


def dfs(self, nums, index, subset, result):
    result.append(subset[:])
    for i in range(index, len(nums)):
        subset.append(nums[i])
        self.dfs(nums, i + 1, subset, result)
        subset.pop()
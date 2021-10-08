def permuteUnique(self, nums: List[int]) -> List[List[int]]:
    nums = sorted(nums)
    visited = [False] * len(nums)
    result = []
    self.dfs(nums, visited, [], result)
    return result


def dfs(self, nums, visited, combo, result):
    if len(combo) == len(nums):
        result.append(combo[:])
        return
    for i in range(len(nums)):
        if visited[i] or (i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]):
            continue
        combo.append(nums[i])
        visited[i] = True
        self.dfs(nums, visited, combo, result)
        combo.pop()
        visited[i] = False

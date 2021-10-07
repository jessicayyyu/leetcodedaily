def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    nums = sorted(candidates)
    result = []
    self.dfs(nums, 0, target, [], result)
    return result


def dfs(self, nums, index, target, combo, result):
    if target < 0:
        return
    if target == 0:
        result.append(list(combo))
    for i in range(index, len(nums)):
        combo.append(nums[i])
        self.dfs(nums, i, target - nums[i], combo, result)
        combo.pop()
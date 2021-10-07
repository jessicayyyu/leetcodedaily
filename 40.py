def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
    nums = sorted(candidates)
    result = []
    self.dfs(nums, 0, target, [], result)
    return result


def dfs(self, nums, index, target, combo, result):
    if target < 0:
        return
    if target == 0:
        result.append(list(combo))
        return
    for i in range(index, len(nums)):
        if nums[i] == nums[i - 1] and i > index:
            continue
        combo.append(nums[i])
        self.dfs(nums, i + 1, target - nums[i], combo, result)
        combo.pop()
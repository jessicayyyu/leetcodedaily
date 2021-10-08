def permute(self, nums: List[int]) -> List[List[int]]:
    result = []
    visited = set()
    self.dfs(nums, [], visited, result)
    return result


def dfs(self, nums, combo, visited, result):
    if len(combo) == len(nums):
        result.append(combo[:])
    for num in nums:
        if num in visited:
            continue
        combo.append(num)
        visited.add(num)
        self.dfs(nums, combo, visited, result)
        combo.pop()
        visited.remove(num)
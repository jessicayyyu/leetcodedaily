def findMaxLength(self, nums: List[int]) -> int:
    for i in range(len(nums)):
        if nums[i] == 0:
            nums[i] = -1
    prefix, res = 0, 0
    hashmap = {}
    hashmap[0] = -1
    for i in range(len(nums)):
        prefix += nums[i]
        if prefix in hashmap:
            res = max(res, i - hashmap.get(prefix))
        else:
            hashmap[prefix] = i
    return res
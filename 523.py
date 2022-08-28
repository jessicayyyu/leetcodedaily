def checkSubarraySum(self, nums: List[int], k: int) -> bool:
    prefix = 0
    hashmap = {}
    hashmap[0] = -1
    for i in range(len(nums)):
        prefix += nums[i]
        if k != 0:
            prefix %= k
        if prefix in hashmap:
            if i - hashmap.get(prefix) > 1:
                return True
        else:
            hashmap[prefix] = i
    return False

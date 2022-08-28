def subarraysDivByK(self, nums: List[int], k: int) -> int:
    hashmap = {}
    hashmap[0] = 1
    prefix, res = 0, 0
    for num in nums:
        prefix = (prefix + num%k + k) % k
        res += hashmap.get(prefix, 0)
        hashmap[prefix] = hashmap.get(prefix, 0) + 1
    return res

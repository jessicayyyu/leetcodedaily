def subarraySum(self, nums: List[int], k: int) -> int:
    prefix_sum = 0
    hashmap = {0:1}
    counter = 0
    for i in range(len(nums)):
        prefix_sum += nums[i]
        #as we added 0 in the beginning, it's important to calculate counter ahead of udpating hashmap, otherwise counter is off by 1
        counter += hashmap.get(prefix_sum - k, 0)
        hashmap[prefix_sum] = hashmap.get(prefix_sum, 0) + 1
    return counter

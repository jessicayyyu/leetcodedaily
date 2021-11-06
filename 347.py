def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    frequencymap = {}
    for num in nums:
        frequencymap[num] = frequencymap.get(num, 0) + 1
    frequencymap = sorted(frequencymap.items(), key = lambda x:x[1], reverse = True)
    res = []
    for i in range(k):
        res.append(frequencymap[i][1])
    return res
import heapq


def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1
    hq = [(val, key) for key, val in freq.items()]
    heapq.heapify(hq)
    while k > 0:
        k -= heapq.heappop(hq)[0]
    return len(hq) + (k < 0)
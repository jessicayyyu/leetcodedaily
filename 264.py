import heapq
def nthUglyNumber(self, n: int) -> int:
    heap = []
    heapq.heappush(heap, 1)
    seen = set()
    seen.add(1)
    factor = [2, 3, 5]
    curr = 1
    for _ in range(n):
        curr = heapq.heappop(heap)
        for f in factor:
            new = curr*f
            if new not in seen:
                seen.add(new)
                heapq.heappush(heap, new)
    return curr


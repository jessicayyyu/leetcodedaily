import heapq
def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
    heap = []
    for point in points:
        d = self.getDistance(point)
        heapq.heappush(heap, (-d, point))
        if len(heap) > K:
            heapq.heappop(heap)
    return [x[1] for x in heap]

def getDistance(self, point):
    return point[0]*point[0] + point[1]*point[1]
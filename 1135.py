import heapq
from collections import deque, defaultdict
class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        G = defaultdict(list)
        for start, end, cost in connections:
            G[start].append((cost, end))
            G[end].append((cost, start))
        total = 0
        q = [(0, n)]
        visited = set()
        while q and len(visited) < n:
            cost, city = heapq.heappop(q)
            if city not in visited:
                visited.add(city)
                total += cost
                for next_cost, next_city in G[city]:
                    heapq.heappush(q, (next_cost, next_city))
        if len(visited) == n:
            return total
        return -1
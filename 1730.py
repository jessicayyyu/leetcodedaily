from collections import deque
d = [(1,0), (-1,0), (0,1), (0,-1)]
class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return -1
        q = deque()
        visited = set()
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "*":
                    q.append((i, j, 0))
                    visited.add((i, j))
        while q:
            x, y, L = q.popleft()
            if grid[x][y] == "#":
                return L
            for dx, dy in d:
                newx, newy = x + dx, y + dy
                if (newx, newy) in visited or newx < 0  or newx >= m or newy < 0 or newy >= n or grid[newx][newy] == "X":
                    continue
                q.append((newx, newy, L + 1))
                visited.add((newx, newy))
        return -1
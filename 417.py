from collections import deque
def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
    if not matrix:
        return []
    m, n = len(matrix), len(matrix[0])
    pacific_starter, atlantic_starter = [], []
    visit_map = {}
    for i in range(m):
        for j in range(n):
            if i == 0 or j == 0:
                pacific_starter.append((i, j))
            if i == m - 1 or j == n - 1:
                atlantic_starter.append((i, j))
    self.bfs(matrix, pacific_starter, visit_map)
    self.bfs(matrix, atlantic_starter, visit_map)
    res = []
    for key, val in visit_map.items():
        if val == 2:
            res.append(list(key))
    return res


def bfs(self, matrix, starter, visit_map):
    m, n = len(matrix), len(matrix[0])
    q = deque(starter)
    visited = set(starter)
    while q:
        cur = q.popleft()
        visit_map[cur] = visit_map.get(cur, 0) + 1
        for dx, dy in dirc:
            newx = cur[0] + dx
            newy = cur[1] + dy
            if newx < 0 or newx >= m or newy < 0 or newy >= n or matrix[newx][newy] < matrix[cur[0]][cur[1]] or (
            newx, newy) in visited:
                continue
            q.append((newx, newy))
            visited.add((newx, newy))
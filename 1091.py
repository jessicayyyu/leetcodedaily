def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
    if grid[0][0] or grid[-1][-1]:
        return -1
    m, n = len(grid), len(grid[0])
    q = deque([(0, 0)])
    distance = {}
    distance[(0, 0)] = 1
    d = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)]
    while q:
        i, j = q.popleft()
        if i == m-1 and j == n-1:
            return distance[(i, j)]
        for dx, dy in d:
            newx = i + dx
            newy = j + dy
            if newx<0 or newx>=m or newy<0 or newy>=n or grid[newx][newy] or (newx, newy) in distance:
                continue
            q.append((newx, newy))
            distance[(newx, newy)] = distance[(i, j)] + 1
    return -1

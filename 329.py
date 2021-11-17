def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
    if not matrix:
        return 0
    m, n = len(matrix), len(matrix[0])
    res = 1
    cache = [[-1]*n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            path = self.dfs(matrix, i, j, m, n, cache)
            res = max(path, res)
    return res

def dfs(self, matrix, i, j, m, n, cache):
    if cache[i][j] != -1:
        return cache[i][j]
    res = 1
    d = [(1,0), (-1,0), (0,1), (0, -1)]
    for dx, dy in d:
        newx, newy = i + dx, j + dy
        if newx < 0 or newx >= m or newy < 0 or newy >= n or matrix[newx][newy] <= matrix[i][j]:
            continue
        path = 1 + self.dfs(matrix, newx, newy, m, n, cache)
        res = max(res, path)
    cache[i][j] = res
    return cache[i][j]

def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
    if not obstacleGrid:
        return 0
    result = self.dfs(obstacleGrid, 0 , 0, {})
    return result

def dfs(self, grid, i, j, memo):
    if grid[i][j]:
        memo[(i, j)] = 0
        return memo[(i, j)]
    if (i, j) in memo:
        return memo[(i, j)]
    m, n = len(grid), len(grid[0])
    if i == m - 1:
        for col in range(j, n):
            if grid[i][col]:
                memo[(i, j)] = 0
                break
        else:
            memo[(i, j)] = 1
        return memo[(i, j)]
    if j == n - 1:
        for row in range(i, m):
            if grid[row][j]:
                memo[(i, j)] = 0
                break
        else:
            memo[(i, j)] = 1
        return memo[(i, j)]
    d = [(1, 0), (0, 1)]
    for dx, dy in d:
        newx, newy = i + dx, j + dy
        if grid[newx][newy]:
            memo[(newx, newy)] = 0
            continue
        memo[(i, j)] += self.dfs(grid, newx, newy, memo)
    return memo[(i, j)]
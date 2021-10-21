def numIslands(self, grid: List[List[str]]) -> int:
    if not grid:
        return 0
    res = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                res += self.dfs(grid, i, j)
    return res

def dfs(self, grid, i, j):
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == '0':
        return 0
    grid[i][j] = '0'
    d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for dx, dy in d:
        newx, newy = i + dx, j + dy
        self.dfs(grid, newx, newy)
    return 1
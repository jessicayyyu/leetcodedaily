def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
    if not grid:
        return 0
    result = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]:
                result = max(result, self.dfs(grid, i, j))
    return result

def dfs(self, grid, i, j):
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or not grid[i][j]:
        return 0
    grid[i][j] = 0
    return 1 + self.dfs(grid, i+1, j)+self.dfs(grid, i-1, j)+self.dfs(grid,i, j+1)+self.dfs(grid,i, j-1)
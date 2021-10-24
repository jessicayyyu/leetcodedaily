def uniquePaths(self, m: int, n: int) -> int:
    result = self.dfs(0, 0, m, n, {})
    return result

def dfs(self, i, j, m, n, memo):
    if (i, j) in memo:
        return memo[(i, j)]
    if i == m - 1 or j == n - 1:
        memo[(i, j)] = 1
        return memo[(i, j)]
    memo[(i, j)] = 0
    memo[(i, j)] += self.dfs(i + 1, j, m, n, memo) + self.dfs(i, j + 1, m, n, memo)
    return memo[(i, j)]
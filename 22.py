def generateParenthesis(self, n: int) -> List[str]:
    result = []
    self.dfs(0, 0, '', n, result)
    return result

def dfs(self, left, right, cur, n, result):
    if left > n or right > n:
        return
    if left < right:
        return
    if left == n and right == n:
        result.append(cur)
    self.dfs(left+1, right, cur+'(',n, result)
    self.dfs(left, right+1, cur+')',n, result)
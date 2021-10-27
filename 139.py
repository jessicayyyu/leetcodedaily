def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    if len(s) == 0:
        return True
    memo = [None] * len(s)
    return self.dfs(s, 0, wordDict, memo)

def dfs(self, s, index, wordset, memo):
    if index == len(s):
        return True
    if memo[index] is not None:
        return memo[index]
    for word in wordset:
        if index + len(word) > len(s):
            continue
        if s[index: index + len(word)] == word:
            if self.dfs(s, index + len(word), wordset, memo):
                memo[index] = True
                return memo[index]
        memo[index] = False
    return  False
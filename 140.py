def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
    maxLen = self.maxLen(wordDict)
    return self.dfs(s, 0, maxLen, wordDict, {})


def dfs(self, s, i, maxLen, wordDict, memo):
    if i == len(s):
        return []
    if s[i:] in memo:
        return memo[s[i:]]

    partitions = []

    if s[i:] in wordDict:
        partitions.append(s[i:])

    for j in range(i, len(s)):
        if j + 1 - i > maxLen:
            break
        prefix = s[i:j + 1]
        if prefix not in wordDict:
            continue
        # print("prefix", prefix)
        sub_part = self.dfs(s, j + 1, maxLen, wordDict, memo)
        # print("sub_part",sub_part)
        for part in sub_part:
            partitions.append(prefix + " " + part)
            # print("ans", partitions)

    memo[s[i:]] = partitions
    return memo[s[i:]]


def maxLen(self, wordDict):
    maxlen = 0
    for word in wordDict:
        maxlen = max(maxlen, len(word))
    return maxlen
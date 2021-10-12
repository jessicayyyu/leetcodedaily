def restoreIpAddresses(self, s: str) -> List[str]:
    results = []
    self.dfs(s, 4, [], results)
    # print(results)
    return ['.'.join(items) for items in results]


def isValid(self, s):
    if s == '0':
        return True
    if s[0] == '0':
        return False
    return 0 <= int(s) <= 255


def dfs(self, s, n, path, results):
    if n == 0:
        if s == "":
            results.append(path[:])
        return

    for i in range(3):
        if i < len(s):
            pre_ip = s[:i + 1]
            if self.isValid(pre_ip):
                path.append(pre_ip)
                self.dfs(s[i + 1:], n - 1, path, results)
                path.pop()
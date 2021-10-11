def isMatch(self, s: str, p: str) -> bool:
    if s == None or p == None:
        return False
    return self.dfs(s, 0, p, 0, {})


def dfs(self, s, sindex, p, pindex, memo):
    if (sindex, pindex) in memo:
        return memo[(sindex, pindex)]

    if pindex == len(p):
        return sindex == len(s)

    if sindex == len(s):
        return self.allStarhelper(p, pindex)

    schar, pchar = s[sindex], p[pindex]

    if pchar == '*':
        match = self.dfs(s, sindex + 1, p, pindex, memo) or \
                self.dfs(s, sindex, p, pindex + 1, memo)
    else:
        match = self.charMatchhelper(schar, pchar) and \
                self.dfs(s, sindex + 1, p, pindex + 1, memo)
    memo[(sindex, pindex)] = match
    return match


def allStarhelper(self, p, pindex):
    for i in range(pindex, len(p)):
        if p[i] != '*':
            return False
    return True


def charMatchhelper(self, schar, pchar):
    return schar == pchar or pchar == '?'
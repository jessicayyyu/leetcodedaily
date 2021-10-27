def isAnagram(self, s: str, t: str) -> bool:
    smapping = {}
    tmapping = {}
    for c in s:
        smapping[c] = smapping.get(c, 0) + 1
    for c in t:
        tmapping[c] = tmapping.get(c, 0) + 1
    return smapping == tmapping
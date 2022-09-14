def groupStrings(self, strings: List[str]) -> List[List[str]]:
    hashmap = defaultdict(list)
    for s in strings:
        key = []
        for i in range(len(s)-1):
            diff = (ord(s[i+1])-ord(s[i]))%26
            key.append(str(diff))
        hashmap[','.join(key)].append(s)
    return list(hashmap.values())

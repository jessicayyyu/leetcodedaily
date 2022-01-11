import collections


def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    hashmap = collections.defaultdict(list)
    for s in strs:
        sortedkey = ''.join(sorted(s))
        hashmap[sortedkey].append(s)
    return hashmap.values()
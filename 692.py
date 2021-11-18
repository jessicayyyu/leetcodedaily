def topKFrequent(self, words: List[str], k: int) -> List[str]:
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    freq = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
    res = []
    for i in range(k):
        res.append(freq[i][0])
    return res
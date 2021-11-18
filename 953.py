def isAlienSorted(self, words: List[str], order: str) -> bool:
    alienorder = {c : i for i, c in enumerate(order)}
    for i in range(len(words)-1):
        word1, word2 = words[i], words[i+1]
        if len(word1) > len(word2) and word1[:len(word2)] == word2:
            return False
        l = min(len(word1), len(word2))
        for j in range(l):
            if word1[j] != word2[j]:
                if alienorder[word1[j]] > alienorder[word2[j]]:
                    return False
                break
    return True
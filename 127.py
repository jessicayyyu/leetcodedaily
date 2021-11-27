from collections import deque
def ladderLength(self, beginWord, endWord, wordList):
    wordList.append(beginWord)
    wordList = set(wordList)
    if endWord not in wordList:
        return 0
    q = deque([(beginWord, 1)])
    visited = set()
    visited.add(beginWord)
    while q:
        word, L = q.popleft()
        if word == endWord:
            return L
        for nex_word in self.get_next_words(word):
            if nex_word not in wordList or nex_word in visited:
                continue
            q.append((nex_word, L + 1))
            visited.add(nex_word)
    return 0

def get_next_words(self, word):
    words = []
    for i in range(len(word)):
        left, right = word[:i], word[i+1:]
        for char in 'abcdefghijklmnopqrstuvwxyz':
            if word[i] == char:
                continue
            words.append(left + char + right)
    return words




class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, word):
        p = self.root
        for c in word:
            if c not in p:
                p[c] = {}
            p = p[c]
        p['#'] = True

    def find(self, word):
        p = self.root
        for c in word:
            if c not in p:
                return None
            p = p[c]
        return p

    def search(self,word):
        node = self.find(word)
        return node and '#' in node

    def startWith(self, prefix):
        return self.find(prefix)

class Trie:
    def __init__(self):
        self.children = {}
        self.word = False

    def insert(self, word: str) -> None:
        if word:
            l = word[0]
            if l not in self.children:
                self.children[l] = Trie()
            self.children[l].insert(word[1:])
        else:
            self.word = True

    def search(self, word: str) -> bool:
        if word:
            l = word[0]
            if l in self.children:
                return self.children[l].search(word[1:])
            else:
                return False
        else:
            return self.word

    def startsWith(self, prefix: str) -> bool:
        if not prefix:
            return True
        l = prefix[0]
        if l in self.children:
            return self.children[l].startsWith(prefix[1:])
        else:
            return False


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

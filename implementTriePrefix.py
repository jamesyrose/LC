class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False


class Trie:

    def __init__(self):
        self.data = TrieNode()

    def insert(self, word: str) -> None:
        buff = self.data
        for l in word:
            if l not in buff.children:
                buff.children[l] = TrieNode()
            buff = buff.children[l]
        buff.end = True

    def search(self, word: str) -> bool:
        buff = self.data
        for l in word:
            if l not in buff.children:
                return False
            buff = buff.children[l]
        return buff.end

    def startsWith(self, prefix: str) -> bool:
        buff = self.data
        for l in prefix:
            if l not in buff.children:
                return False
            buff = buff.childrern[l]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

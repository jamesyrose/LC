class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False


class WordDictionary:

    def __init__(self):
        self.data = TrieNode()

    def addWord(self, word: str) -> None:
        buff = self.data
        for l in word:
            if l not in buff.children:
                buff.children[l] = TrieNode()
            buff = buff.children[l]
        buff.end = True

    def search(self, word: str) -> bool:
        def dfs(j, root):
            node = root
            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for l in node.children.values():
                        if dfs(i + 1, l):
                            return True
                    return False
                else:
                    if c not in node.children:
                        return False
                    node = node.children[c]
            return node.end
        return dfs(0, self.data)



if __name__ == "__main__":
    action =["WordDictionary", "addWord", "addWord", "search", "search", "search", "search", "search", "search"]
    word = [[], ["a"], ["a"], ["."], ["a"], ["aa"], ["a"], [".a"], ["a."]]
    null = None
    false = False
    true = True
    ans  = [null,null,null,true,true,false,true,false,false]

    wdict = WordDictionary()
    res = [None]
    for a, w in zip(action, word):
        if a == "addWord":
            res.append(wdict.addWord(w[0]))
        elif a == "search":
            res.append(wdict.search(w[0]))
    print(ans)
    print(res, res == ans)

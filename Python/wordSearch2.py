class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
        self.word = ""

    def add_word(self, word):
        cur = self
        for l in word:
            if l not in cur.children:
                cur.children[l] = TrieNode()
            cur = cur.children[l]
        cur.word = word
        cur.end = True


class Solution:
    def findWords(self, board: list, words: list) -> list:
        """
        O(n * m * 4^max(len(word))) Time

        :param board:
        :param words:
        :return:
        """
        trie = TrieNode()
        for word in words:
            trie.add_word(word)
        visit = set()
        found = set()

        def dfs(i, j, node):
            if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or (i, j) in visit or board[i][
                j] not in node.children:
                return

            visit.add((i, j))
            node = node.children[board[i][j]]
            if node.end:
                found.add(node.word)

            dfs(i + 1, j, node)
            dfs(i - 1, j, node)
            dfs(i, j + 1, node)
            dfs(i, j - 1, node)
            visit.remove((i, j))
            return
        for i in  range(len(board)):
            for j in range(len(board[0])):
                visit = set()
                dfs(i, j, trie)
        return list(found)


if __name__ == "__main__":
    board = [["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]]
    words = ["oath", "pea", "eat", "rain", "hklf", "hf"]
    ans = ["eat", "oath"]
    resp = Solution().findWords(board, words)
    if ans == resp:
        print("PASS", resp)
    else:
        print("FAIL", resp)

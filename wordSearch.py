class Solution:
    def exist(self, board: list, word: str) -> bool:
        """
        O(n * m * 4^len(word)) Time
        O(n * m ) space
        :param board:
        :param word:
        :return:
        """
        starting_points = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    starting_points.append([i, j])

        visit = set()
        def dfs(i, j, remaining):
            if  (i, j) in visit or i < 0  or i >= len(board) or 0 > j or j >= len(board[0]):
                return False
            if remaining == "":
                return True
            elif board[i][j] != remaining[0]:
                return False
            elif len(remaining) == 1 and board[i][j] == remaining:
                return True


            remaining = remaining[1:]
            visit.add((i, j))
            if dfs(i + 1, j, remaining):
                return True
            if dfs(i - 1, j, remaining):
                return True
            if dfs(i , j + 1, remaining):
                return True
            if dfs(i, j - 1 , remaining):
                return True
            visit.remove((i, j))
            return False

        for start in starting_points:
            if dfs(start[0], start[1], word):
                return True
        return False





if __name__ == "__main__":
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "SEE"
    ans = True
    resp = Solution().exist(board, word)
    if ans == resp:
        print("PASS", resp)
    else:
        print("FAIL", resp)

class Solution:
    def generateParenthesis(self, n: int) -> list:
        """
        DFS solution

        :param n:
        :return:
        """
        res = set()

        def dfs(s, open, left):
            if left == 0 and open == 0:
                res.add(s)
                return
            if open < 0 or left == 0 :
                return
            dfs(s + "(", open + 1, left - 1)
            dfs(s + ")", open - 1, left - 1)
            return

        dfs("(", 1, n  * 2 - 1)
        return list(res)

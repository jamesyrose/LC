class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        O(n * m ) time
        O(n) space

        :param m:
        :param n:
        :return:
        """
        dp_last = [1] * n
        for i in range(m - 2, -1, -1):
            dp_temp = [1] * (n + 1)
            for j in range(n - 2, -1, -1):
                dp_temp[j] = dp_last[j] + dp_temp[j + 1]
            dp_last = dp_temp
        return dp_last[0]

    def mathematicalWay(self, m: int, n: int) -> int:
        import math
        return int(math.factorial(m + n - 2) / (math.factorial((m - 1)) * math.factorial(n - 1)))

    def usingDFS(self, m: int, n: int) -> int:
        """
        brute force
        :return:
        """

        def dfs(m, n):
            if m == 0 or n == 0:
                return 1
            return dfs(m - 1, n) + dfs(m, n - 1)

        return dfs(m - 1, n - 1)


if __name__ == "__main__":
    n = 7
    m = 3
    ans = 28
    resp = Solution().uniquePaths(m, n)
    if ans == resp:
        print("PASS", resp)
    else:
        print("FAIL", resp)

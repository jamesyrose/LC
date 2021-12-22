class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        N, M = len(grid), len(grid[0])
        dp = [[float("infinity") for _ in range(M)] for _ in range(N)]

        for i in range(N):
            for j in range(M):
                if i == 0 and j == 0:
                    dp[i][j] = grid[i][j]
                elif i == 0 and j != 0:
                    dp[i][j] = dp[i][j - 1] + grid[i][j]
                elif i != 0 and j == 0:
                    dp[i][j] = dp[i - 1][j] + grid[i][j]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        return dp[N - 1][M - 1]



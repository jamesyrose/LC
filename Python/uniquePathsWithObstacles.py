class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        N, M = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for _ in range(M + 1)] for _ in range(N + 1)]
        dp[N - 1][M - 1] = 1

        for i in range(N - 1, -1, -1):
            for j in range(M - 1, -1, -1):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    if i == N - 1 and j == M - 1:
                        continue
                    dp[i][j] = dp[i + 1][j] + dp[i][j + 1]

        return dp[0][0]


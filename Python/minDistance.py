class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        N, M = len(word1), len(word2)
        dp = [[0 for _ in range(M)] for _ in range(N)]
        for i in range(N):
            dp[i].append(N - i)
        dp.append([i for i in range(M, -1, -1)])

        for i in range(N - 1, -1, -1):
            for j in range(M - 1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    dp[i][j] = min(dp[i][j + 1], dp[i + 1][j], dp[i + 1][j + 1]) + 1
        return dp[0][0]

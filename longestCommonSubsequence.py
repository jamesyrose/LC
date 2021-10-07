class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        O(nm)
        :param text1:
        :param text2:
        :return:
        """
        # rows of text 1
        # columns of text 2
        dp = [[0] * (len(text2) + 1)] * (len(text1) + 1)

        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = dp[i + 1][j + 1] + 1
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
        return dp[0][0]
if __name__ == "__main__":
    text1 = "abcba"
    text2 = "abcbcba"
    ans = 5
    resp = Solution().longestCommonSubsequence(text1, text2)
    if ans == resp:
        print("PASS", resp)
    else:
        print("FAIL", resp)


class Solution:
    def wordBreak(self, s: str, wordDict: list) -> bool:
        """
        O(n^2) time
        O(n) space
        :param s:
        :param wordDict:
        :return:
        """
        dp = [False] * (len(s) + 1 )
        dp[-1] = True
        for i in range(len(s) - 1, -1, -1):
            letter = s[i]
            for word in wordDict:
                if letter == word[0] and len(dp) - i > len(word):
                    if s[i: i + len(word)] == word and dp[i + len(word) ]:
                        dp[i] = True
        return dp[0]




if __name__ == "__main__":
    s = "leetcode"
    wordDict = ["leet", "code"]
    ans = False
    resp = Solution().wordBreak(s, wordDict)
    if ans == resp:
        print("PASS", resp)
    else:
        print("FAIL", resp)


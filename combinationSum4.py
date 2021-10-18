class Solution:
    def combinationSum4(self, nums: list, target: int) -> int:
        """
        O(n*m)
        :param nums:
        :param target:
        :return:
        """
        dp = {0: 1}

        for i in range(1, target + 1):
            dp[i] = 0
            for num in nums:
                dp[i] += dp.get(i - num, 0)
        return dp[target]



if __name__ == "__main__":
    nums = [1,2,3]
    target = 4
    ans = 7
    resp = Solution().combinationSum4(nums, target)
    if ans == resp:
        print("PASS", resp)
    else:
        print("FAIL", resp)


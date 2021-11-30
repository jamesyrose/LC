class Solution:
    def rob(self, nums: list) -> int:
        """
        O(n)
        :param nums:
        :return:
        """
        dp = nums + [0,0,0]
        for i in range(len(nums) - 1, -1,-1):
            dp[i] = dp[i] + max(dp[i + 2], dp[i + 3])
        return max(dp)

    def rob2(self, nums: list ) -> int:
        """
        O(n)

        :param nums:
        :return:
        """
        l1_max = self.rob(nums[1:])
        l2_max = self.rob(nums[:-1])
        return max(l1_max, l2_max)


if __name__ == "__main__":
    nums = [1,2,3,1]
    ans = 4
    resp = Solution().rob2(nums)
    if ans == resp:
        print("PASS", resp)
    else:
        print("FAIL", resp)


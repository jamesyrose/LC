class Solution:
    def lengthOfLIS(self, nums: list) -> int:
        """
        O(n^2)
        :param nums:
        :return:
        """
        dp = [1] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)






if __name__ == "__main__":
    nums = [1,3,6,7,9,4,10,5,6]
    ans = 6
    resp = Solution().lengthOfLIS(nums)
    if ans == resp:
        print("PASS", resp)
    else:
        print("FAIL", resp)


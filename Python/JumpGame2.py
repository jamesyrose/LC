class Solution:
    def canJump(self, nums: list) -> int:
        """
        O(n) time
        O(n) space

        :param nums:
        :return:
        """
        dp = [1e5] * len(nums)
        dp[-1]  = 0

        for i in range(len(nums) - 2, -1, -1):
            curr_jump = nums[i]
            if curr_jump + i > len(nums):
                dp[i] = 1
            else:
                dp[i] = min(dp[i + 1: i + curr_jump + 1]) + 1
        return dp[0]



if __name__ == "__main__":
    nums = [2,3,1,1,4]
    ans = 2
    resp = Solution().canJump(nums)
    if ans == resp:
        print("PASS", resp)
    else:
        print("FAIL", resp)


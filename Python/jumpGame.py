class Solution:
    def canJump(self, nums: list) -> bool:
        """
        O(n) time
        O(n) space

        :param nums:
        :return:
        """
        dp = [False] * len(nums)
        dp[-1]  = True

        for i in range(len(nums) - 2, -1, -1):
            curr_jump = nums[i]
            if curr_jump + i > len(nums):
                dp[i] = True
            elif any(dp[i + 1: i + curr_jump + 1]):
                dp[i] = True
        return dp[0]



if __name__ == "__main__":
    nums = [3,2,1,0,4]
    ans = False
    resp = Solution().canJump(nums)
    if ans == resp:
        print("PASS", resp)
    else:
        print("FAIL", resp)


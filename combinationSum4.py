class Solution:
    def combinationSum4(self, nums: list, target: int) -> int:
        """
        O(n^2)
        :param nums:
        :param target:
        :return:
        """
        dp = [0] * (target + 1)

        for i in range(1, target):
            for num in nums:
                if i - num >= 0:
                    dp[i] += 1  + dp[i - num]
        print(dp)
        return dp[-2]



if __name__ == "__main__":
    nums = [1,2,3]
    target = 4
    ans = 7
    resp = Solution().combinationSum4(nums, target)
    if ans == resp:
        print("PASS", resp)
    else:
        print("FAIL", resp)


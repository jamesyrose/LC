class Solution:
    def maxSubArray(self, nums: list) -> int:
        curr_max = nums[0]
        curr = 0

        for n in nums:
            if curr < 0:
                curr = 0
            curr += n
            curr_max = max(curr, curr_max)

        return curr_max


if __name__ == "__main__":
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    ans = 6
    resp = Solution().maxSubArray(nums)
    if ans == resp:
        print("PASS", resp)
    else:
        print("FAIL", resp)

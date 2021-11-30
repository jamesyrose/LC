class Solution:
    def maxProduct(self, nums: list) -> int:
        """
        O(n)

        :param nums:
        :return:
        """
        max_val = 1
        min_val = 1
        res = max(nums)
        for num in nums:
            if num == 0:
                max_val = 1
                min_val = 1
            else:
                temp = max_val
                max_val = max(num,  max_val * num, min_val * num)
                min_val = min(num, temp * num, min_val * num)
                if max_val > res:
                    res = max_val
        return res


if __name__ == "__main__":
    nums = [3,-1,4]
    ans = 4
    resp = Solution().maxProduct(nums)
    if ans == resp:
        print("PASS", resp)
    else:
        print("FAIL", resp)

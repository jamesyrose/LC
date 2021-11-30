class Solution:
    def search(self, nums: list, target: int) -> int:
        """
        O(log n)

        :param nums:
        :param target:
        :return:
        """
        l, r = 0, len(nums) - 1

        while l <= r:
            midpnt = (l + r) // 2
            # Check midpnt
            if target == nums[midpnt]:
                return midpnt
            # if there are only 2 elements just check each
            if r - l <= 2:
                if nums[l] == target:
                    return l
                elif nums[r] == target:
                    return r
                else:
                    return -1
            if nums[l] < nums[midpnt]:
                if nums[l] > target or target > nums[midpnt]:
                    l = midpnt + 1
                else:
                    r = midpnt - 1
            else:
                if nums[r] < target or nums[midpnt] > target:
                    r = midpnt - 1
                else:
                    l = midpnt + 1
        return -1


if __name__ == "__main__":
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0
    ans = 4
    resp = Solution().search(nums, target)
    if ans == resp:
        print("PASS", resp)
    else:
        print("FAIL", resp)

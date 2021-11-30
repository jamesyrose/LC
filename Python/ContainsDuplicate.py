class Solution:
    def containsDuplicate(self, nums: list) -> bool:
        """
        O(n)

        set function iterates (O(n)) and add (O(1))

        :param nums:
        :return:
        """
        if len(set(nums)) == len(nums):  # set functions time complexity is O(n)
            return False
        return True


if __name__ == "__main__":
    nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    ans = True
    resp = Solution().containsDuplicate(nums)
    if ans == resp:
        print("PASS", resp)
    else:
        print("FAIL", resp)

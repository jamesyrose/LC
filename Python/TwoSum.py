class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        """
        O(n)
        :param nums:
        :param target:
        :return:
        """
        table = {}
        for i in range(len(nums)): # O(n)
            remain = target - nums[i]
            if remain in table.keys(): # O(1)
                return [table[remain], i]
            table[nums[i]] = i

if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    ans = [0, 1]
    resp = Solution().twoSum(nums, target)
    if ans == resp:
        print("PASS", resp)
    else:
        print("FAIL", resp)
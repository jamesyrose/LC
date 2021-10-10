class Solution:
    def longestConsecutive(self, nums: list) -> int:
        uniq_num = set(nums)
        max_consecutive = 0
        for num in nums:
            count = 1
            if num - 1 not in uniq_num:
                while True:
                    num += 1
                    if num not in uniq_num:
                        break
                    count += 1
            if count > max_consecutive:
                max_consecutive = count
        return max_consecutive

if __name__ == "__main__":
    nums = [100, 4, 200, 1, 3, 2]
    ans = 4
    resp = Solution().longestConsecutive(nums)

    if ans == resp:
        print("PASS", resp)
    else:
        print("FAIL", resp)

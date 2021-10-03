class Solution:
    def productExceptSelf(self, nums: list) -> list:
        zero_cnt = 0
        zero_idx = None
        total_mult = 1
        for i in range(len(nums)):
            num = nums[i]
            if num == 0:
                zero_cnt += 1
                zero_idx = i
            else:
                total_mult *= num
            if zero_cnt > 1:
                return [0] * len(nums)
        if zero_cnt == 1:
            out_arr = [0] * len(nums)
            out_arr[zero_idx] = total_mult
        else:
            out_arr = [int(total_mult / nums[i]) for i in range(len(nums))]
        return out_arr


if __name__ == "__main__":
    nums = [-1, 1, 0, -3, 3]
    ans = [0, 0, 9, 0, 0]
    resp = Solution().productExceptSelf(nums)
    if ans == resp:
        print("PASS", resp)
    else:
        print("FAIL", resp)

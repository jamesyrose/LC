class Solution:
    def threeSum(self, nums: list) :
        """
        O(n log n) time
        :param nums:
        :return:
        """
        res = []
        nums  = sorted(nums)

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) -1
            while l < r:
                three_sum = a + nums[l] + nums[r]
                if three_sum > 0 :
                    r -=1
                elif three_sum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l -1] and l < r:
                        l += 1
        return res



if __name__ == "__main__":
    nums = [-1,0,1,2,-1,-4]
    ans = [[-1,-1,2],[-1,0,1]]
    resp = Solution().threeSum(nums)
    if ans == resp:
        print("PASS", resp)
    else:
        print("FAIL", resp)

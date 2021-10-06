class Solution:
    def threeSum(self, nums: list) :
        def twoSum(nums, target):
            table = {}
            for i in range(len(nums)):  # O(n)
                remain = target - nums[i]
                if remain in table.keys():  # O(1)
                    return [table[remain], i]
                table[nums[i]] = i
            return - 1
        ans = []
        nums_sort = sorted(nums)
        for i in range(len(nums_sort)):
            target = nums_sort[i]
            twos = twoSum(nums_sort, target)
            if twos != -1:
                ans.append([target, nums_sort[twos[0]], nums_sort[twos[1]]])
        return ans



if __name__ == "__main__":
    nums = [-1,0,1,2,-1,-4]
    ans = [[-1,-1,2],[-1,0,1]]
    resp = Solution().threeSum(nums)
    if ans == resp:
        print("PASS", resp)
    else:
        print("FAIL", resp)

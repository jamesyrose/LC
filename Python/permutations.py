class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        nums = set(nums)
        res = []

        def dfs(curr, nums):
            if len(nums) == 0:
                c = curr[:]  # copy
                res.append(c)
                return

            for n in list(nums):
                curr.append(n)
                nums.remove(n)
                dfs(curr, nums)
                curr.pop()
                nums.add(n)

        dfs([], nums)
        return res



class Solution:
    def topKFrequent(self, nums: list, k: int) -> list:
        """
        O(n) time  and space
        :param nums:
        :param k:
        :return:
        """

        res = {}
        for num in nums:  # O(n)
            if num in res:
                res[num] += 1
            else:
                res[num] = 1
        out = [[] for _ in range(len(nums) + 1)]
        for key, v in res.items():
            out[v].append(key)
        ans = []
        for vals in reversed(out):
            if len(ans) < k:
                ans += vals
            else:
                return ans
        return ans

    def topKFrequent2(self, nums: list, k: int) -> list:
        """
        O(n log n) time
        O(n) space
        :param nums:
        :param k:
        :return:
        """

        res = {}
        for num in nums:  # O(n)
            if num in res:
                res[num] += 1
            else:
                res[num] = 1
        sort = sorted(zip(res.values(), res.keys()), key=lambda pair: pair[0])  # O(n log n)
        ans = []
        for i in range(1, k + 1):  # O(k)
            ans.append(sort[-i][1])
        return ans


if __name__ == "__main__":
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    ans = [1, 2]

    resp = Solution().topKFrequent(nums, k)

    if ans == resp:
        print("PASS", resp)
    else:
        print("FAIL", resp)

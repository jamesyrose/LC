class Solution:
    def groupAnagrams(self, strs: list) -> list:
        """
        O(n * m) time where n = len(strs) m = avgs(strs[i])
        """
        from collections import defaultdict
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - 97] += 1
            res[tuple(count)].append(s)
        return list(res.values())


if __name__ == "__main__":
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    ans = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
    resp = Solution().groupAnagrams(strs)
    if ans == resp:
        print("PASS", resp)
    else:
        print("FAIL", resp)

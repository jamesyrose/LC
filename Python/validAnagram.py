class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        O(n) time
        O(n) space
        :param s:
        :param t:
        :return:
        """
        if len(s) != len(t):
            return False
        res = {}
        for i in range(len(s)):
            if s[i] not in res:
                res[s[i]] = 1
            else:
                res[s[i]] += 1
            if t[i] not in res:
                res[t[i]] = -1
            else:
                res[t[i]] -= 1
        return True if not any(res.values()) else False

    def isAnagram2(self, s: str, t: str) -> bool:
        """
        Cheap trick
        Counter time complexity o(n)
        :param s:
        :param t:
        :return:
        """
        from collections import Counter
        return Counter(s) == Counter(t)


if __name__ == "__main__":
    s = "anagram"
    t = "nagaram"
    ans = True
    resp = Solution().isAnagram2(s, t)
    if ans == resp:
        print("PASS", resp)
    else:
        print("FAIL", resp)

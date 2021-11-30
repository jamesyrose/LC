class Solution:
    def numDecodings(self, s: str) -> int:
        """
        O(n) time
        O(1) space
        :param s:
        :return:
        """
        # cannot decode with leading 0
        if s[0] == "0":
            return 0
        d1 = 1
        d2 = 1
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                curr = 0
            else:
                curr = d1
            if i + 1 < len(s) and (s[i] == "1") or (s[i] == "2" and s[i + 1] in "0123456"):
                curr = d1 + d2

            buff = d1
            d1 = curr
            d2 = buff
        return d1


if __name__ == "__main__":
    s = "123101234"
    ans = 5
    resp = Solution().numDecodings(s)
    if ans == resp:
        print("PASS", resp)
    else:
        print("FAIL", resp)

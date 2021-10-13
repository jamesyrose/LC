class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        O(n) time
        O(k) space, where k = len(t)

        :param s:
        :param t:
        :return:
        """

        have, need = {}, {}
        if len(t) == 1:
            return t if t in s else ""

        for i in range(len(t)):
            if t[i] in need:
                need[t[i]] += 1
            else:
                need[t[i]] = 1
                have[t[i]] = 0

        l = 0
        have_cnt = 0
        need_cnt = len(need)
        idx, minLen = [0, 0], 1e6
        for r in range(len(s)):
            if s[r] in have:
                have[s[r]] += 1
                if have[s[r]] == need[s[r]]:
                    have_cnt += 1
            while have_cnt == need_cnt:
                if (r - l + 1) < minLen:
                    idx = [l, r + 1]
                    minLen = (r - l + 1)

                if s[l] in have:
                    have[s[l]] -= 1
                    if have[s[l]] < need[s[l]]:
                        have_cnt -= 1
                l += 1
        return s[idx[0]:idx[1]]


if __name__ == "__main__":
    s = "a"
    t = "aa"
    ans = "abbbbbcdd"
    resp = Solution().minWindow(s, t)
    if ans == resp:
        print("PASS", resp)
    else:
        print("FAIL", resp)

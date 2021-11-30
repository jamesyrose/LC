class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        O(n) time # while loop
        O(n) space # set

        :param s:
        :return:
        """
        # base base:
        if len(s) <=1:
            return len(s)
        p1, p2 = 0, 0
        longest  = 0
        letters = set()
        while p2 < len(s) and p1< len(s):
            if s[p2] in letters:
                letters.remove(s[p1])
                p1 += 1
            else:
                letters.add(s[p2])
                p2 += 1
                longest = max(p2 -p1, longest)
        return longest





if __name__ == "__main__":
    s  = "abcabcbb"
    ans = 3
    resp = Solution().lengthOfLongestSubstring(s)
    if ans == resp:
        print("PASS", resp)
    else:
        print("FAIL", resp)
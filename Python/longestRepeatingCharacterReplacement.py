class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        O(26n)
        O(26) space

        :param s:
        :param k:
        :return:
        """

        def change_counts(letter, dir=1):
            """
            helper function for adding to dict
            """
            if letter in counts:
                counts[letter] += dir
            else:
                counts[letter] = 1

        # base case
        if len(s) <= 1:
            return len(s)
        l, r = 0, 1
        longest = 0
        counts = {s[0]: 1}

        while r < len(s):
            if (sum(counts.values()) - max(counts.values())) <= k:
                change_counts(s[r])
                r += 1
                if sum(counts.values()) - max(counts.values()) <= k:
                    longest = max(longest, sum(counts.values()))
            else:
                change_counts(s[l], dir=-1)
                l += 1
        return longest


if __name__ == "__main__":
    s = "AABABBA"
    k = 1
    ans = 4
    resp = Solution().characterReplacement(s, k)
    if ans == resp:
        print("PASS", resp)
    else:
        print("FAIL", resp)

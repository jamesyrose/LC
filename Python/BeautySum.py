class Solution:
    def beautySum(self, s: str) -> int:
        """O(n ^ 2) time O(1) space"""
        beauty = {}  # max size is 26
        total = 0

        for i in range(len(s)):
            beauty[s[i]] = beauty.get(s[i], 0) + 1
            for j in range(i + 1, len(s)):
                beauty[s[j]] = beauty.get(s[j], 0) + 1
                b_max = max(beauty.values())
                b_min = min(beauty.values())
                if b_min != 0:
                    total += (b_max - b_min)
            for j in range(i + 1, len(s)):
                # reset back
                beauty[s[j]] -= 1
                if beauty[s[j]] == 0:
                    del beauty[s[j]]

            beauty[s[i]] -= 1
            if beauty[s[i]] == 0:
                del beauty[s[i]]

        return total





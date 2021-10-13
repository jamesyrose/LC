class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""
        long_len = 0

        for i in range(len(s)):
            max_pali = min(i, len(s) - i)
            j = 1
            print(s[i], s[i -j], s[i + j])
            while j < max_pali and s[i -j] == s[i + j]:
                j += 1
            if 2 * j  - 1 >long_len:
                long_len = 2 * j -1
                longest = s[i -j: i +j]
        return longest


    def bruteForce(self, s: str):
        """
        O(n^3)
        :param s:
        :return:
        """
        longest = ""
        long_len = 0
        for i in range(len(s)):
            for j in range (len(s) , i, -1):
                curr = s[i:j]
                if curr == curr[::-1] and len(curr) > long_len:
                    longest =  curr
                    long_len = len(curr)
        return longest

if __name__ == "__main__":
    s = "cbbd"
    ans = "bab"
    resp = Solution().longestPalindrome(s)
    if ans == resp:
        print("PASS", resp)
    else:
        print("FAIL", resp)

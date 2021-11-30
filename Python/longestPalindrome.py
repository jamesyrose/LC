class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        O(n^2) time
        O(1)

        :param s:
        :return:
        """
        longest = [-1, -1]
        long_len = 0

        for i in range(len(s)): # O(n)
            l, r = i, i
            while l >= 0  and r < len(s) and s[l]  == s[r]: # O(n)
                if (r - l + 1) >  long_len:
                    longest = [l,r + 1]
                    long_len = r - l  + 1
                l -=1
                r += 1
            l, r =  i, i + 1
            while l >= 0  and r < len(s) and s[l]  == s[r]: # O(n)
                if (r - l + 1) >  long_len:
                    longest = [l,r + 1]
                    long_len = r - l  + 1
                l -=1
                r += 1
        return s[longest[0]:longest[1]]


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

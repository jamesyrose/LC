class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        O(36n) -> O(n) time

        clearest approach
        :param s:
        :return:
        """
        forward = ""
        for c in s:
            if c.lower().isalnum():
                forward += c.lower()
        return forward == forward[::-1]

    def isPalindrome2(self, s: str) -> bool:
        """
        O(n) time

        :param s:
        :return:
        """
        s = ''.join([x.lower() for x in s if x.isalnum()])
        return s == s[::-1]


if __name__ == "__main__":
    s = "A man, a plan, a canal: Panama"
    ans = False
    resp = Solution().isPalindrome(s)
    if ans == resp:
        print("PASS", resp)
    else:
        print("FAIL", resp)

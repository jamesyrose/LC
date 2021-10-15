class Solution:
    def countSubstrings(self, s: str) -> int:

        """
        O(n^2) time
        O(1)

        :param s:
        :return:
        """
        count  = 0

        for i in range(len(s)): # O(n)
            l, r = i, i
            while l >= 0  and r < len(s) and s[l]  == s[r]: # O(n)
                count += 1
                l -=1
                r += 1
            l, r =  i, i + 1
            while l >= 0  and r < len(s) and s[l]  == s[r]: # O(n)
                count += 1
                l -=1
                r += 1
        return count

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
    s = "abc"
    ans =  3
    resp = Solution().countSubstrings(s)
    if ans == resp:
        print("PASS", resp)
    else:
        print("FAIL", resp)

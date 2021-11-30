class Solution:
    def climbStairs(self, n: int) -> int:
        """
        Fibonacci sequence
        :param n:
        :return:
        """
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 2
        a, b = 1, 1
        for i  in range(n-1):
            buff = a
            a = a + b
            b = buff
        return a

if __name__ == "__main__":
    n = 5
    ans = 8
    resp = Solution().climbStairs(n)
    if ans == resp:
        print("PASS", resp)
    else:
        print("FAIL", resp)
class Solution:
    """binary leet code problem"""
    def hammingWeight(self, n: int) -> int:
        """
        Taking the & of each binary with one 1 in it,
        if it equals to the original, then that bit is 1, add 1 to count

        :param n:
        :return:
        """
        count = 0
        for i in range(32, -1, -1):
            temp = 2 ** i
            if n & temp == temp:
                count +=1
        return count


    def hammingWeight2(self, n: int) -> int:
        """Feels like cheating because of using - operator """
        count = 0
        for i in range(32, -1, -1):
            if n - 2 ** i >= 0 :
                n -= 2 ** i
                count += 1
        return count


    def hammingWeight3(self, n: int) -> int:
        """Feels like cheating to use strings"""
        return sum([a=="1" for a in bin(n)])


if __name__ == "__main__":
    a = 128
    ans = 1
    resp = Solution().hammingWeight(a)
    if ans == resp:
        print("PASS", resp)
    else:
        print("FAIL", resp)

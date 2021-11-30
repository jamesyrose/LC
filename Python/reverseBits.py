class Solution:
    def reverseBits(self, n: int) -> int:
        """& for each bit, if it equals the bit, then add it's reverse to the output"""
        res = 0
        for i in range(32, -1, -1):
            temp = 2 ** i
            if n & temp == temp:
                res += 2 ** (32-i-1)
        return res

    def reverseBits2(self, n: int) -> int:
        """kind of cheating to just reverse a string"""
        return int('{:032b}'.format(n)[::-1],2)


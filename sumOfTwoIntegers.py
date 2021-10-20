class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xffffffff  # limit int size to 32 bit to handle overflow
        while b & mask:
            xor = a ^ b  # Xor
            carry = (a & b) << 1  # and  + shift 1

            a, b = xor, carry
        return (a & mask) if b > 0 else a


if __name__ == "__main__":
    a = 1
    b = 5
    ans = 3
    resp = Solution().getSum(a, b)
    if ans == resp:
        print("PASS", resp)
    else:
        print("FAIL", resp)

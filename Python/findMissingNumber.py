class Solution:
    """binary leet code problem"""
    def missingNumber(self, nums: list) -> int:
        """XOR repetively, if the number exists, it will return binary of 0, the one unique number will be left"""
        missed = len(nums)
        for i, n in enumerate(nums):
            missed = missed ^ (n ^i) #  missed + (i - n) basically
        return missed


    def missingNumber2(self, nums: list) -> int:
        """ a little cheating"""
        n = set(nums)
        for i in range(len(nums) + 1):
            if i not in n:
                return i

if __name__ == "__main__":
    a = [3,0,1]
    ans = 2
    resp = Solution().missingNumber(a)
    if ans == resp:
        print("PASS", resp)
    else:
        print("FAIL", resp)

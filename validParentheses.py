class Solution:
    def isValid(self, s: str) -> bool:
        """
        O(n) time
        O(n) space
        :param s:
        :return:
        """
        opn = {"[": "]", "(": ")", "{": "}"}

        stack = []
        for c in s:
            if c in opn:
                stack.append(c)
            elif len(stack) == 0:
                return False
            elif c == opn[stack[-1]]:
                stack.pop(-1)
            else:
                return False
        return True if len(stack) == 0 else False



if __name__ == "__main__":
    s = "(])"
    ans = False
    resp = Solution().isValid(s)
    if ans == resp:
        print("PASS", resp)
    else:
        print("FAIL", resp)

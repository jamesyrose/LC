class Solution:
    def calculate(self, s: str) -> int:
        """
        O(n) time
        O(n) space

        :param s:
        :return:
        """

        stack = []

        sign = "+"
        num = ""

        for i in range(len(s)):
            c = s[i]
            if c in ["+", "-", "*", "/"] or i == len(s) - 1:
                if i == len(s) - 1:
                    num += c
                tmp = int(num)
                if sign == "+":
                    stack.append(tmp)
                elif sign == "-":
                    stack.append(-tmp)
                elif sign == "*":
                    stack[-1] *= tmp
                elif sign == "/":
                    last = stack[-1]
                    if last < 0:
                        # true div works right with positive
                        stack[-1] = - (-last // tmp)
                    else:
                        stack[-1] = last // tmp
                num = ""
                sign = c
            else:
                num += c

        return sum(stack)

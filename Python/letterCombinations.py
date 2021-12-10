class Solution:
    def letterCombinations(self, digits: str) :
        if digits == "":
            return []
        letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        res = [""]
        tmp = []

        for d in digits:
            ls = list(letters[d])
            for exist in res:
                for l in ls:
                    tmp.append(exist + l)
            res = tmp
            tmp = []
        return res


if __name__ == "__main__":
    nums = "23"
    ans = ["ad","ae","af","bd","be","bf","cd","ce","cf"]
    resp = Solution().letterCombinations(nums)
    if ans == resp:
        print("PASS", resp)
    else:
        print("FAIL", resp)
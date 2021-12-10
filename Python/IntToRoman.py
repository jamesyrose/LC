class Solution:
    def intToRoman(self, num: int) -> str:
        """
        O(n) time
        """
        map = {
            "1": "I",
            "4": "IV",
            "5": "V",
            "9": "IX",
            "10": "X",
            "40": "XL",
            "50": "L",
            "90": "XC",
            "100": "C",
            "400": "CD",
            "500": "D",
            "900": "CM",
            "1000": "M"
        }
        zeros = ""
        ans = ""

        num = str(num)
        for c in reversed(num):
            if c in  map:
                c += zeros
                ans = map[c] + ans
            else:
                c = int(c)
                tmp = ""
                if c >= 5:
                    c -= 5
                    tmp  += map["5" + zeros]
                while c > 0:
                    c -= 1
                    tmp += map["1" + zeros]
                ans = tmp + ans
            zeros += "0"
        return ans







if __name__ == "__main__":
    nums = 1994
    ans = "MCMXCIV"
    resp = Solution().intToRoman(nums)
    if ans == resp:
        print("PASS", resp)
    else:
        print("FAIL", resp)

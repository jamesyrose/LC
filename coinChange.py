class Solution:
    def coinChange(self, coins:list, amount: int) -> int:
        """
        O(n * m)

        :param coins:
        :param amount:
        :return:
        """

        arr = [amount + 1] * (amount + 1)
        arr[0] = 0
        for i in range(1, amount + 1):
            for j in range(len(coins)):
                if coins[j] <= i:
                    arr[i] = min(arr[i], arr[i - coins[j]] + 1)
        return arr[amount] if arr[amount] != amount + 1 else -1






if __name__ == "__main__":
    coins = [1, 2, 5]
    amount = 11
    ans = 3
    resp = Solution().coinChange(coins, amount)
    if ans == resp:
        print("PASS", resp)
    else:
        print("FAIL", resp)

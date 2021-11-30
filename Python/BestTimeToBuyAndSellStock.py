class Solution:
    def maxProfit(self, prices: list) -> int:
        """
        O(n)
        :param prices:
        :return:
        """
        max_profit = 0
        high = 0
        # iterate backwards, find the high value, iterate backwards more,
        # check the difference if difference exceeds previous max_profit update it
        for i in range(len(prices) - 1, -1, -1): # O(n)
            if prices[i] > high: # new high value
                high = prices[i]
            else:
                profit = high - prices[i] # current to last seen high
                if profit > max_profit: # update if greater than seen max_profit
                    max_profit = profit
        return max_profit

if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]
    ans = 5
    resp = Solution().maxProfit(prices)
    if ans == resp:
        print("PASS", resp)
    else:
        print("FAIL", resp)

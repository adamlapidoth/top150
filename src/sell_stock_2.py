from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        You are given an integer array prices where prices[i] is the price of
        a given stock on the ith day.
        On each day, you may decide to buy and/or sell the stock.
        You can only hold at most one share of the stock at any time.
        However, you can buy it then immediately sell it on the same day.
        Find and return the maximum profit you can achieve.
        :param prices: Array of prices
        :return: The max profit. if no profit can be achieved returns 0
        """
        max_profit = 0
        for i in range(len(prices) - 1):
            profit = prices[i + 1] - prices[i]
            if profit > 0:
                max_profit += profit
        return max_profit

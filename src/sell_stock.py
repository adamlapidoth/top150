from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        You are given an array prices where prices[i] is the price of a given
        stock on the ith day.
        You want to maximize your profit by choosing a single day to buy one
        stock and choosing a different day in the future to sell that stock.
        Return the maximum profit you can achieve from this transaction.
         f you cannot achieve any profit, return 0.
        :param prices: Array of numbers
        :return: The max profit. if no profit is possible return 0
        """
        max_profit = 0
        buy = prices[0]  # current lowest price
        for i in range(1, len(prices)):
            if prices[i] < buy:
                # found lower price
                buy = prices[i]
            elif prices[i] - buy > max_profit:
                # if current price is greater then previous buy and profit is
                # greater than max profit then maximize profit
                max_profit = prices[i] - buy
        return max_profit

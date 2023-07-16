from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        You are given an array prices where prices[i] is the price of a given
        stock on the ith day.
        You want to maximize your profit by choosing a single day to buy one
        stock and choosing a different day in the future to sell that stock.
        Return the maximum profit you can achieve from this transaction.
        if you cannot achieve any profit, return 0.
        :param prices: Array of numbers
        :return: The max profit. if no profit is possible return 0
        """
        max_profit = 0
        lowest_price = prices[0]
        for price in prices:
            if price < lowest_price:
                lowest_price = price
            if price - lowest_price > max_profit:
                max_profit = price - lowest_price
        return max_profit

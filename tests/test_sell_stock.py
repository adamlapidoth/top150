from sell_stock import Solution


def test_max_profit_1():
    s = Solution()
    max_profit = s.maxProfit(prices=[7, 1, 5, 3, 6, 4])
    assert max_profit == 5


def test_max_profit_2():
    s = Solution()
    max_profit = s.maxProfit(prices=[7, 6, 4, 3, 1])
    assert max_profit == 0

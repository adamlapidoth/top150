from sell_stock_2 import Solution


def test_max_profit_1():
    s = Solution()
    max_profit = s.maxProfit([7, 1, 5, 3, 6, 4])
    assert max_profit == 7


def test_max_profit_2():
    s = Solution()
    max_profit = s.maxProfit([1, 2, 3, 4, 5])
    assert max_profit == 4


def test_max_profit_3():
    s = Solution()
    max_profit = s.maxProfit([7, 6, 4, 3, 1])
    assert max_profit == 0

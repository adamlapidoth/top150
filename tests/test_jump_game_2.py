from jump_game_2 import Solution


def test_jump_1():
    s = Solution()
    min_jumps = s.jump([2, 3, 1, 1, 4])
    assert min_jumps == 2


def test_jump_2():
    s = Solution()
    min_jumps = s.jump([2, 3, 0, 1, 4])
    assert min_jumps == 2

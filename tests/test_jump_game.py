from jump_game import Solution


def test_can_jump_1():
    s = Solution()
    assert s.canJump([2, 3, 1, 1, 4])


def test_can_jump_2():
    s = Solution()
    assert not s.canJump([3, 2, 1, 0, 4])

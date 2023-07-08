from rotate_array import Solution


def test_rotate_1():
    s = Solution()
    nums = [1, 2, 3, 4, 5, 6, 7]
    s.rotate(nums, k=3)
    assert nums == [5, 6, 7, 1, 2, 3, 4]


def test_rotate_2():
    s = Solution()
    nums = [-1, -100, 3, 99]
    s.rotate(nums, k=2)
    assert nums == [3, 99, -1, -100]

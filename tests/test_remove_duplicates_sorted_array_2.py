from remove_duplicates_sorted_array_2 import Solution


def test_remove_duplicates_1():
    s = Solution()
    nums = [1, 1, 1, 2, 2, 3]
    k = s.removeDuplicates(nums)
    assert k == 5
    assert nums[:k] == [1, 1, 2, 2, 3]


def test_remove_duplicates_2():
    s = Solution()
    nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    k = s.removeDuplicates(nums)
    assert k == 7
    assert nums[:k] == [0, 0, 1, 1, 2, 3, 3]

from remove_element import Solution


def test_remove_element_1():
    s = Solution()
    nums = [3, 2, 2, 3]
    k = s.removeElement(nums=nums, val=3)
    assert k == 2
    assert sorted(nums[:k]) == sorted([2, 2])


def test_remove_element_2():
    s = Solution()
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    k = s.removeElement(nums=nums, val=2)
    assert k == 5
    assert sorted(nums[:k]) == sorted([2, 2])

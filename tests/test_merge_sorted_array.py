from merge_sorted_array import Solution


def test_merge_1():
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    s = Solution()
    s.merge(nums1, m, nums2, n)
    assert nums1 == [1, 2, 2, 3, 5, 6]


def test_merge_2():
    nums1 = [1]
    m = 1
    nums2 = []
    n = 0
    s = Solution()
    s.merge(nums1, m, nums2, n)
    assert nums1 == [1]


def test_merge_3():
    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    s = Solution()
    s.merge(nums1, m, nums2, n)
    assert nums1 == [1]


def test_merge_4():
    nums1 = [4, 5, 6, 0, 0, 0]
    m = 3
    nums2 = [1, 2, 3]
    n = 3
    s = Solution()
    s.merge(nums1, m, nums2, n)
    assert nums1 == [1, 2, 3, 4, 5, 6]

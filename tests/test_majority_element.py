from majority_element import Solution


def test_majority_element_1():
    s = Solution()
    m_e = s.majorityElement(nums=[3, 2, 3])
    assert m_e == 3


def test_majority_element_2():
    s = Solution()
    m_e = s.majorityElement(nums=[2, 2, 1, 1, 1, 2, 2])
    assert m_e == 2

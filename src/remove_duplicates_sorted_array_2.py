from collections import Counter
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Remove some duplicates in-place such that each unique element appears
        at most twice.
        The relative order of the elements should be kept the same.
        :param nums: A sorted array with duplicates
        :return: The number of elements. Each element can have at most 2
        duplicates.
        """
        c = Counter(nums)
        for num in c:
            if c[num] > 2:
                c[num] = 2
        nums[:] = sorted(c.elements())
        return len(nums)

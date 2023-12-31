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
        i = 0
        for e in nums:
            if i == 0 or i == 1 or nums[i - 2] != e:
                nums[i] = e
                i += 1
        return i

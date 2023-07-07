from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Remove duplicates from a sorted array
        :param nums: A sorted array with duplicates
        :return: The number of unique elements.
        nums should be changed in-place so that unique elements appear
        only once.
        """
        my_set = set(nums)
        nums[:] = sorted(my_set)
        return len(my_set)

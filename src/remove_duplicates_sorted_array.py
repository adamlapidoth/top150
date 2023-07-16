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
        i = 0
        for e in nums:
            if i == 0 or nums[i - 1] != e:
                nums[i] = e
                i += 1
        return i

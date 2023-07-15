from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        Given an integer array nums and an integer val, remove all occurrences
        of val in nums in-place.
        :param nums:An array of numbers
        :param val: The value to remove
        :return: The number of elements in nums which are not equal to val.
        nums will be changed in-place so that all elements that are not equal
        to val will be first (order is not important)
        """
        if not nums:
            return 0
        i, j = 0, len(nums) - 1
        while i <= j:
            if nums[i] == val and nums[j] != val:
                nums[i], nums[j] = nums[j], nums[i]
            if nums[i] != val:
                i += 1
            if nums[j] == val:
                j -= 1
        return i

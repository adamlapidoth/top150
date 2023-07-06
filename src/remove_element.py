from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """

        :param nums:An array of numbers
        :param val: The value to remove
        :return: The number of elements in nums which are not equal to val.
        nums will be changed in-place so that all elements that are not equal
        to val will be first (order is not important)
        """
        res = 0
        nums_tmp = []
        for x in nums:
            if x != val:
                res += 1
                nums_tmp.append(x)
        nums[:] = nums_tmp
        return res

from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Rotate array to the right k times. do it in place.
        :param nums: A list of numbers
        :param k: Number of places to rotate to the right
        """
        length = len(nums)
        nums[:] = nums[length - k % length:] + nums[:length - k % length]

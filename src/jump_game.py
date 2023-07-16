from typing import List, Optional


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        You are given an integer array nums. You are initially positioned at
        the array's first index, and each element in the array represents your
        maximum jump length at that position.
        :param nums: An array of numbers
        :return: True if it is possible to reach last index, False otherwise
        """
        pos = len(nums) - 1
        for i in range(pos, 0, -1):
            if nums[i - 1] + i - 1 >= pos:
                pos = i - 1
        return pos == 0

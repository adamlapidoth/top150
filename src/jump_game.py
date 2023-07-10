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
        goal = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0

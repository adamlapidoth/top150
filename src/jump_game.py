from typing import List, Optional


class Solution:
    def can_jump_helper(self, goal: int, nums: List[int]) -> Optional[int]:
        """
        A helper method that returns the index from where you can jump
        to the goal.
        :param goal: The goal of the jump game
        :param nums: An array of numbers
        :return: The index of the array where jump to the goal is possible.
        If reaching to goal is not possible from any index None is returned.
        """
        for i, n in enumerate(nums):
            if nums[i] + i >= goal:
                return i
        return None

    def canJump(self, nums: List[int]) -> bool:
        """
        You are given an integer array nums. You are initially positioned at
        the array's first index, and each element in the array represents your
        maximum jump length at that position.
        :param nums: An array of numbers
        :return: True if it is possible to reach last index, False otherwise
        """
        goal = len(nums) - 1
        new_goal = self.can_jump_helper(goal, nums)
        while new_goal:
            new_goal = self.can_jump_helper(goal=new_goal, nums=nums[:new_goal])
        if new_goal == 0:
            return True
        return False




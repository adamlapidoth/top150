from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        You are given a 0-indexed array of integers nums of length n.
        You are initially positioned at nums[0]. Each element nums[i]
        represents the maximum length of a forward jump from index i.
        In other words, if you are at nums[i], you can jump to any nums[i + j]
        where:
        0 <= j <= nums[i] and
        i + j < n
        :param nums: Array of numbers
        :return: The minimum number of jumps to reach last index.
        """
        n = len(nums)
        i, last_pos, max_pos, jump = 0, 0, 0, 0
        while i < n - 1:
            max_pos = max(nums[i] + i, max_pos)
            if i == last_pos:
                last_pos = max_pos
                jump += 1
            i += 1
        return jump

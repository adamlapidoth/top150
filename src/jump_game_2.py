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
        dp = [float("inf") for _ in range(n)]
        dp[0] = 0  # init DP array [0, inf, inf, inf, ...]

        for i in range(n):
            for j in range(1, nums[i] + 1):
                if i + j < n:
                    dp[i + j] = min(dp[i + j], dp[i] + 1)

        return int(dp[-1])

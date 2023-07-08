from collections import Counter
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        Given an array nums of size n, return the majority element.
        The majority element is the element that appears more than n / 2 times.
        You may assume that the majority element always exists in the array.
        :param nums: List of numbers
        :return: The majority element
        """
        counter = Counter(nums)
        for num in counter:
            if counter[num] >= len(nums) / 2:
                return num
        raise ValueError(
            "The List of numbers doesn't have a majority element"
        )  # if code reached this point
        # there was an error in the nums parameter

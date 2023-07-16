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
        votes = 0
        candidate = None
        for n in nums:
            if votes == 0:
                candidate = n
                votes = 1
            elif candidate == n:
                votes += 1
            else:
                votes -= 1
        return candidate

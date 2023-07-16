from typing import List


class Solution:
    def merge(
        self, nums1: List[int], m: int, nums2: List[int], n: int
    ) -> None:
        """
        Merge nums1 and nums2 into a single array sorted in non-decreasing
        order. Do not return anything, modify nums1 in-place instead.
        :param nums1: A sorted array (non decreasing order).
        :param m: Length of relevant numbers
        :param nums2: A sorted array (non decreasing order).
        :param n: Length of nums 2
        :return: None. The resulting sorted array will be stored in nums1.
        To accommodate this nums1 will have the length of m+n and the
        last n elements will be set to 0 and should be ignored
        """
        i, j = m - 1, n - 1
        z = m + n - 1
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[z] = nums1[i]
                i -= 1
            else:
                nums1[z] = nums2[j]
                j -= 1
            z -= 1
        while j >= 0:
            nums1[z] = nums2[j]
            z -= 1
            j -= 1

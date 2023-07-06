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
        res = []
        i, j = 0, 0
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                res.append(nums1[i])
                i += 1
            else:
                res.append(nums2[j])
                j += 1
        if i == m:
            res.extend(nums2[j:])
        else:
            res.extend(nums1[i:])
        nums1[:] = res[: m + n]

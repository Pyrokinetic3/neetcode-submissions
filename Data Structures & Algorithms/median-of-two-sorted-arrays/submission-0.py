class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        list = nums1 + nums2
        sort = sorted(list)
        if len(sort) % 2 == 0:
            return (sort[len(sort) // 2  - 1] + sort[len(sort) // 2]) / 2
        else:
            return sort[len(sort) // 2]
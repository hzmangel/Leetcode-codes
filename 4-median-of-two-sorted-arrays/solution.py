class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        len_1 = len(nums1)
        idx_1 = 0

        len_2 = len(nums2)
        idx_2 = 0

        total_len = len_1 + len_2
        mid_len = total_len / 2
        total_len_is_odd = (total_len % 2 == 1)
        mid_val = None

        rslt = []
        rslt_len = 0

        while True:
            if idx_1 >= len_1:
                rslt.append(nums2[idx_2])
                idx_2 += 1
            elif idx_2 >= len_2:
                rslt.append(nums1[idx_1])
                idx_1 += 1
            elif nums1[idx_1] <= nums2[idx_2]:
                rslt.append(nums1[idx_1])
                idx_1 += 1
            elif nums1[idx_1] > nums2[idx_2]:
                rslt.append(nums2[idx_2])
                idx_2 += 1

            rslt_len += 1

            if rslt_len > mid_len:
                break

        if total_len_is_odd:
            return rslt[rslt_len-1]
        else:
            return (rslt[rslt_len-1] + rslt[rslt_len-2])/2.0


foo = Solution()
print(foo.findMedianSortedArrays([1, 2], [3, 4]) == 2.5)
print(foo.findMedianSortedArrays([1, 3], [2]) == 2.0)
print(foo.findMedianSortedArrays([1], [1]) == 1.0)


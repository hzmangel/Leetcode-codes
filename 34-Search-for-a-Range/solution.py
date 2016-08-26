class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        start_idx = 0
        end_idx = len(nums)
        rslt = None

        while True:
            mid_idx = (start_idx + end_idx) / 2
            mid_val = nums[mid_idx]

            if mid_val == target:
                low_idx = start_idx
                high_idx = end_idx-1

                for i in xrange(mid_idx-1, start_idx-1, -1):
                    if nums[i] < target:
                        low_idx = i+1
                        break

                for i in xrange(mid_idx, end_idx):
                    if nums[i] > target:
                        high_idx = i-1
                        break

                rslt = [low_idx, high_idx]
                break

            elif mid_val < target:
                start_idx = mid_idx

            elif mid_val > target:
                end_idx = mid_idx

            if ((end_idx - start_idx) == 1) or (start_idx >= end_idx):
                if nums[start_idx] == target:
                    rslt = [start_idx, end_idx-1]
                    break
                else:
                    rslt = [-1, -1]
                    break

        return rslt
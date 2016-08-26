class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        return self.splitSearch(nums, target, 0, len(nums))

    def splitSearch(self, nums, target, start_pos, end_pos):
        if start_pos >= end_pos or len(nums) == 1:
            return [-1, -1]

        if len(nums) == 2:
            if nums[0] > target or nums[1] < target:
                return [-1, -1]
            else:
                if nums[0] == target:
                    if nums[1] == target:
                        return [0, 1]
                    else:
                        return [0, 0]
                elif nums[1] == target:
                    return [1, 1]
                else:
                    return [-1, -1]

        mid_idx = (start_pos + end_pos) / 2
        mid_val = nums[mid_idx]

        if mid_val == target:
            low_idx = start_pos
            high_idx = end_pos

            for i in xrange(mid_idx-1, start_pos-1, -1):
                if nums[i] < target:
                    low_idx = i+1
                    break

            for i in xrange(mid_idx, end_pos):
                if nums[i] > target:
                    high_idx = i-1
                    break

            return [low_idx, high_idx]

        elif mid_val < target:
            self.splitSearch(nums, target, mid_idx, end_pos)
        elif mid_val > target:
            self.splitSearch(nums, target, start_pos, mid_idx)

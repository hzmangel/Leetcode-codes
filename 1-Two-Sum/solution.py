class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_count = len(nums)

        for idx1, v1 in enumerate(nums):
            to_be_found = target - v1
            for idx2, v2 in enumerate(nums[idx1+1:]):
                if v2 == to_be_found:
                    return [idx1, idx2+idx1+1]

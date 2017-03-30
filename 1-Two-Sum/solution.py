class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        rslt = {}

        for i, num in enumerate(nums):
            if num in rslt:
                return (i, rslt[num])
            else:
                rslt[target - num] = i


foo = Solution()
print(foo.twoSum([2, 7, 11, 15], 9))

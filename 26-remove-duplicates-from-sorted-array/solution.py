class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if nums is None:
            return None

        array_len = len(nums)
        if array_len == 0 or array_len == 1:
            return array_len

        last_val_idx = 0  # Index for last value

        for i in range(1, array_len):
            if nums[last_val_idx] != nums[i]:
                last_val_idx += 1
                nums[last_val_idx] = nums[i]

        # last_val_idx is from 0, so add 1 offset for length
        return last_val_idx + 1

foo = Solution()
print(foo.removeDuplicates([1]))
print(foo.removeDuplicates([1,1,2,2]))
print(foo.removeDuplicates([1,1,2,2,3,3,3,4,4,4,4]))


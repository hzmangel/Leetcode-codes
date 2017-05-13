class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        if nums is None or val is None:
            return None

        arr_length = len(nums)
        rslt = arr_length

        for i in range(arr_length):
            if nums[i] == val:
                nums[i] = None
                rslt -= 1

        last_idx = arr_length - 1  # Last index of array element
        for i in range(arr_length):
            if nums[i] is None:
                while nums[last_idx] is None and i  < last_idx:
                    last_idx -= 1

                if i >= last_idx:
                    # The backward point has already crossed with forward index,
                    # all the elements from forward index are None, break.
                    break
                else:
                    # Backward index still has element, swap them
                    nums[i] = nums[last_idx]
                    last_idx -= 1

        return rslt



foo = Solution()
nums = [1]
print(foo.removeElement(nums, 1), nums)

nums = [3,2,2,3]
print(foo.removeElement(nums, 1), nums)

nums = [3,2,3,3,2,2,3]
print(foo.removeElement(nums, 2), nums)


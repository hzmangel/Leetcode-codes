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

        if arr_length == 1:
            if nums[0] == val:
                nums = []
                return 0
            else:
                return 1

        r_idx = arr_length - 1  # Right index of array elements
        for l_idx in range(arr_length):
            if l_idx > r_idx:
                # The backward point has already crossed with forward index,
                # all the elements from forward index are the given value,
                # break.
                break
            elif l_idx == r_idx:
                if nums[l_idx] == val:
                    rslt -= 1

                break
            else:
                if nums[l_idx] == val:
                    rslt -= 1
                    while nums[r_idx] == val and l_idx < r_idx:
                        r_idx -= 1
                        rslt -= 1

                    if l_idx < r_idx:
                        # Backward index still has element, swap them
                        nums[l_idx], nums[r_idx] = nums[r_idx], nums[l_idx]
                        r_idx -= 1

        return rslt


foo = Solution()
nums = [1]
print(foo.removeElement(nums, 1), nums)

nums = [1,2]
print(foo.removeElement(nums, 1), nums)

nums = [1,2]
print(foo.removeElement(nums, 2), nums)

nums = [3,2,2,3]
print(foo.removeElement(nums, 1), nums)

nums = [3,2,2,3]
print(foo.removeElement(nums, 3), nums)

nums = [3,2,3,3,2,2,3]
print(foo.removeElement(nums, 2), nums)


class Solution(object):
    # @profile
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        nums.sort()
        arr_len = len(nums)

        rslt = []
        for idx in range(arr_len - 2):
            num = nums[idx]
            if idx > 0 and num == nums[idx - 1]:
                continue

            target_val = 0 - num
            l_idx, r_idx = idx + 1, arr_len - 1

            while (l_idx < r_idx):
                if l_idx == idx or r_idx == idx:
                    break

                tmp_sum = nums[l_idx] + nums[r_idx]
                if tmp_sum == target_val:
                    rslt.append(tuple(sorted([nums[l_idx], nums[r_idx], num])))
                    curr_l = nums[l_idx]
                    curr_r = nums[r_idx]

                    while((l_idx < arr_len) and (nums[l_idx] == curr_l)):
                        l_idx += 1

                    while((r_idx > 0) and (nums[r_idx] == curr_r)):
                        r_idx -= 1

                elif tmp_sum < target_val:
                    l_idx += 1
                elif tmp_sum > target_val:
                    r_idx -= 1

        return rslt


foo = Solution()
print(foo.threeSum([0] * 1000))

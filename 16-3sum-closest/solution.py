class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        arr_len = len(nums)
        if (arr_len == 3):
            return sum(nums)

        nums.sort()
        rslt = sum(nums[0:3])

        for i in range(arr_len - 2):
            j, k = i + 1, arr_len - 1

            while(j < k):
                tmp_sum = nums[i] + nums[j] + nums[k]
                if tmp_sum == target:
                    return target

                if abs(tmp_sum - target) < abs(rslt - target):
                    rslt = tmp_sum

                if tmp_sum < target:
                    j += 1

                if tmp_sum > target:
                    k -= 1

        return rslt


foo = Solution()
print(foo.threeSumClosest([1,1,1,0], -100) == 2)
print(foo.threeSumClosest([1,1,1,0], 100) == 3)
print(foo.threeSumClosest([0,2,1,-3], 1) == 0)
print(foo.threeSumClosest([1,1,-1,-1,3], -1) == -1)
print(foo.threeSumClosest([1,2,4,8,16,32,64,128], 82) == 82)
print(foo.threeSumClosest([1,2,5,10,11], 12) == 13)
print(foo.threeSumClosest([0,0,0], 1) == 0)
print(foo.threeSumClosest([1,1,1,1], 0) == 3)

import cProfile as profile


class Solution(object):

    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        rslt = 0
        data_len = len(height)
        l = 0
        h = data_len - 1

        while(l < h):
            if (height[l] <= height[h]):
                new_area = height[l] * (h - l)
                l += 1
            else:
                new_area = height[h] * (h - l)
                h -= 1

            if new_area > rslt:
                rslt = new_area

        return rslt


foo = Solution()
print(foo.maxArea([3, 4]) == 3)
#print(foo.maxArea([1, 1]) == 1)
#print(foo.maxArea([1, 2, 4, 3]) == 4)

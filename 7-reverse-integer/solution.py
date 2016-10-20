class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        rslt = 0
        signed = False

        if (x < 0):
            signed = True
            x = -x

        while x != 0:
            rslt *= 10
            rslt += x % 10
            x = int(x/10)

        if signed:
            rslt = -rslt

        if rslt > 2**31-1 or rslt < -2**31:
            rslt = 0

        return rslt

foo = Solution()
print(foo.reverse(123) == 321)
print(foo.reverse(-123) == -321)
print(foo.reverse(0) == 0)
print(foo.reverse(10) == 1)
print(foo.reverse(1234567890) == 987654321)
print(foo.reverse(1534236469) == 0)
print(foo.reverse(1563847412) == 0)
print(foo.reverse(-2147483648) == 0)


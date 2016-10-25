class Solution(object):
    def myAtoi(self, s):
        """
        :type str: str
        :rtype: int
        """
        s = s.strip()
        sign = 1
        rslt = 0

        if len(s) == 0:
            return 0

        if s[0] == '-':
            sign = -1
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]

        if len(s) == 0:
            return 0

        for c in s:
            try:
                rslt = rslt * 10 + int(c)
            except ValueError:
                break

        rslt *= sign
        if rslt > 2**31-1:
            return 2**31-1
        elif rslt < -2**31:
            return -2**31
        else:
            return rslt

foo = Solution()
print(foo.myAtoi('') == 0)
print(foo.myAtoi('a') == 0)
print(foo.myAtoi('  -0012a42') == -12)
print(foo.myAtoi('+1') == 1)
print(foo.myAtoi('2147483648') == 2147483647)

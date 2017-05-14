class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        if haystack is None or needle is None:
            return None

        haystack_len = len(haystack)
        needle_len = len(needle)

        if needle_len > haystack_len:
            return -1

        for idx in range(haystack_len - needle_len + 1):
            if haystack[idx:idx + needle_len] == needle:
                return idx

        return -1


foo = Solution()
print(foo.strStr(None, None))
print(foo.strStr(None, 'abc'))
print(foo.strStr('abcdefg', None))
print(foo.strStr('a', 'abcd'))
print(foo.strStr('abcdefg', 'abc'))
print(foo.strStr('decgab', 'abc'))

import cProfile as profile
import timeit


class Solution(object):

    def findPalindrome(self, s, l_end_idx, r_start_idx):
        offset = 0
        max_len = r_start_idx - l_end_idx + 1
        str_len = len(s)

        while l_end_idx - offset >= 0 and r_start_idx + offset < str_len:
            if s[l_end_idx - offset] == s[r_start_idx + offset]:
                max_len += 2
                offset += 1
            else:
                return max_len, s[l_end_idx-offset+1:r_start_idx+offset]

        return max_len, s[l_end_idx-offset+1:r_start_idx+offset]

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        if s is None or len(s) == 1:
            return s

        str_len = len(s)
        max_len = 0
        rslt = ''

        for idx, c in enumerate(s):
            tmp_max_len, tmp_rslt = self.findPalindrome(s, idx-1, idx+1)
            if tmp_max_len > max_len:
                max_len = tmp_max_len
                rslt = tmp_rslt

            tmp_max_len, tmp_rslt = self.findPalindrome(s, idx, idx+1)
            if tmp_max_len > max_len:
                max_len = tmp_max_len
                rslt = tmp_rslt

        return rslt

foo = Solution()
print(foo.longestPalindrome('b') == 'b')
print(foo.longestPalindrome('bb') == 'bb')
print(foo.longestPalindrome('abcbe') == 'bcb')
print(foo.longestPalindrome('abccbe') == 'bccb')
print(foo.longestPalindrome('abcabcba') == 'abcba')
print(foo.longestPalindrome('abcdcbaabc') == 'abcdcba')
print(foo.longestPalindrome('aabbccbbaa') == 'aabbccbbaa')
print(foo.longestPalindrome("abababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababa") == "abababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababa")

print(timeit.timeit('foo.longestPalindrome("abababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababa")', setup="from __main__ import Solution; foo = Solution()", number=50))

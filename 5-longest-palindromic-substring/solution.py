import cProfile as profile
import timeit


class Solution(object):

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        max_len = 0
        rslt = ''
        str_len = len(s)

        for idx, c in enumerate(s):
            if max_len == 0:
                max_len = 1
                rslt = c

            if(idx >= 1) and (idx + 1 < str_len) and (s[idx - 1] == s[idx + 1]):
                i = 0

                first_half = s[:idx][::-1]
                second_half = s[idx + 1:]
                limit = min(len(first_half), len(second_half))

                for i in range(limit):
                    if first_half[i] != second_half[i]:
                        i -= 1
                        break

                i += 1
                if 2 * i + 1 > max_len:
                    max_len = 2 * i + 1
                    rslt = s[idx - i:idx + i + 1]

            if(idx + 1 < str_len) and (s[idx] == s[idx + 1]):
                i = 0
                first_half = s[:idx+1][::-1]
                second_half = s[idx + 1:]
                limit = min(len(first_half), len(second_half))

                for i in range(limit):
                    if first_half[i] != second_half[i]:
                        i -= 1
                        break

                if 2 * (i + 1) > max_len:
                    max_len = 2 * (i + 1)
                    rslt = s[idx - i:idx + 1 + i + 1]

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

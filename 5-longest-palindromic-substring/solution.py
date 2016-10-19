class Solution(object):

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        max_len = 0
        rslt = ''
        str_len = len(s)
        palindrom_str_len = 0
        palindrom_str = ''

        # if str_len == 1:
        #   return s

        for idx, c in enumerate(s):
            if max_len == 0:
                max_len = 1
                rslt = c

            if(idx >= 1) and (idx + 1 < str_len) and (s[idx - 1] == s[idx + 1]):
                i = 1
                while (idx >= i and idx + i < str_len and s[idx - i] == s[idx + i]):
                    i += 1

                i -= 1
                if 2 * i + 1 > max_len:
                    max_len = 2 * i + 1
                    rslt = s[idx - i:idx + i + 1]


            if(idx + 1 < str_len) and (s[idx] == s[idx + 1]):
                i = 0
                while (idx >= i and idx + i + 1 < str_len and s[idx - i] == s[idx + 1 + i]):
                    i += 1

                i -= 1
                if 2 * (i+1) > max_len:
                    max_len = 2 * (i + 1)
                    rslt = s[idx - i:idx + 1 + i + 1]


        return rslt

foo = Solution()
print(foo.longestPalindrome('b') == 'b')
print(foo.longestPalindrome('bb') == 'bb')
print(foo.longestPalindrome('abcabcba') == 'abcba')
print(foo.longestPalindrome('abcdcbaabc') == 'abcdcba')
print(foo.longestPalindrome("abababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababa") == "abababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababa")

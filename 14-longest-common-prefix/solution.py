import cProfile as profile


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        if len(strs) == 0:
            return ''

        rslt = strs[0]

        for s in strs[1:]:
            str_len = len(s)
            for idx, c in enumerate(rslt):
                if idx >= str_len or s[idx] != c:
                    rslt = rslt[:idx]
                    break

        return ''.join(rslt)


foo = Solution()
print(foo.longestCommonPrefix(['ab', 'a']))

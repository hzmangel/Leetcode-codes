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
            tmp_rslt = []
            str_len = len(s)
            for idx, c in enumerate(rslt):
                if idx >= str_len or s[idx] != c:
                    break
                tmp_rslt.append(c)

            rslt = tmp_rslt

        return ''.join(rslt)


foo = Solution()
print(foo.longestCommonPrefix(['ab', 'a']))

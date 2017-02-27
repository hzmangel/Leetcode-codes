class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        if digits == '':
            return []

        ch_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }

        rslt = [[]]
        for c in digits:
            rslt = [x+[y] for x in rslt for y in ch_map[c]]

        return tuple([''.join(r) for r in rslt])


foo = Solution()
print(foo.letterCombinations('234'))

import collections

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """

        if s is None:
            return

        rslt = collections.defaultdict(int)
        for c in s:
            rslt[c] += 1

        odds = [i for i in rslt.values() if i % 2 == 1]
        evens = [i for i in rslt.values() if i % 2 == 0]

        # Choose one odds character as middle, then choose other odd characters
        # count - 1 time.

        odds_len = 0
        if len(odds) > 0:
            odds_len = (sum(odds) - len(odds) + 1)

        return odds_len + sum(evens)


foo = Solution()
print(foo.longestPalindrome(None))
print(foo.longestPalindrome(''))
print(foo.longestPalindrome('a'))
print(foo.longestPalindrome('abccccdd'))
print(foo.longestPalindrome('aabbccdd'))

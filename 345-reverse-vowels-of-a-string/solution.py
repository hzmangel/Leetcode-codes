import re


class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """

        vowels_pattern = re.compile(r'[aeiouAEIOU]')

        if s is None or s == '':
            return s

        vowels_found = [m.start(0) for m in vowels_pattern.finditer(s)]
        new_s = list(s)

        for idx in range(len(vowels_found) // 2):
            new_s[vowels_found[idx]], new_s[vowels_found[-1-idx]] = new_s[vowels_found[-1-idx]], new_s[vowels_found[idx]]

        return ''.join(new_s)


foo = Solution()
print(foo.reverseVowels('leetcode'))

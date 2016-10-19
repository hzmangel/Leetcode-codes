class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        sub_set = set()
        sub_list = []
        length_list = []

        for idx, c in enumerate(s):
            if c in sub_set:
                length_list.append(len(sub_list))
                sub_list = sub_list[sub_list.index(c) + 1:]
                sub_list.append(c)
                sub_set = set(sub_list)
            else:
                sub_list.append(c)
                sub_set.add(c)

        length_list.append(len(sub_list))
        return max(length_list)


foo = Solution()
print(foo.lengthOfLongestSubstring('a'))
print(foo.lengthOfLongestSubstring('aab'))
print(foo.lengthOfLongestSubstring('aaaaa'))
print(foo.lengthOfLongestSubstring('abcabcabcs'))


class Solution(object):

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        if len(s) % 2 == 1:
            return False
        check_stack = []
        ch_map = {
            '(': 1,
            ')': -1,
            '[': 2,
            ']': -2,
            '{': 3,
            '}': -3,
        }
        for c in s:
            ch_val = ch_map[c]
            if ch_val > 0:
                check_stack.append(ch_val)
            else:
                if check_stack == [] or ch_val + check_stack.pop() != 0:
                    return False

        return check_stack == []


foo = Solution()
print(foo.isValid('{}{}[]()') == True)
print(foo.isValid('{{(}}[]()') == False)
print(foo.isValid('{') == False)
print(foo.isValid('}{') == False)
print(foo.isValid('((') == False)

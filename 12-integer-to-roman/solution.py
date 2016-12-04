class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        roman_num_table = (
            (1000, ('M', 1000)),
            (100, ('C', 100), ('D', 500), ('M', 1000)),
            (10, ('X', 10), ('L', 50), ('C', 100)),
            (1, ('I', 1), ('V', 5), ('X', 10)),
        )

        rslt = []
        for idx, level in enumerate(roman_num_table):
            cnt = int(num / level[0])
            if cnt == 0:
                continue

            if cnt == 5:
                rslt.append('{}'.format(level[2][0]))
            elif cnt == 4:
                rslt.append('{}{}'.format(level[1][0], level[2][0]))
            elif cnt == 9:
                rslt.append('{}{}'.format(level[1][0], level[3][0]))
            elif cnt < 4:
                rslt.append(('{0}'*cnt).format(level[1][0]))
            elif cnt > 5:
                rslt.append(('{0}' + '{1}'*(cnt-5)).format(level[2][0], level[1][0]))

            num = num % level[0]

        return ''.join(rslt)


foo = Solution()
print(foo.intToRoman(4) == 'IV')
print(foo.intToRoman(5) == 'V')
print(foo.intToRoman(6) == 'VI')
print(foo.intToRoman(76) == 'LXXVI')
print(foo.intToRoman(99) == 'XCIX')
print(foo.intToRoman(499) == 'CDXCIX')
print(foo.intToRoman(3888) == 'MMMDCCCLXXXVIII')
print(foo.intToRoman(3999) == 'MMMCMXCIX')



class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        if numRows == 1:
            return s

        str_len = len(s)

        if numRows > str_len:
            return s

        loop_count = int(str_len / numRows)+1
        slice_length = 2 * numRows - 2

        idx_list = []

        for i in range(numRows):
            if i == 0:
                idx_list.append([slice_length * lc for lc in range(loop_count)])
            elif i == (numRows - 1):
                idx_list.append([slice_length * lc + i for lc in range(loop_count)])
            else:
                idx_list.append([idx for sublist in [(slice_length * lc + i, slice_length * (lc+1) - i) for lc in range(loop_count)] for idx in sublist])

        flatten_idx = [idx for sublist in idx_list for idx in sublist if idx < str_len]
        return ''.join([s[idx] for idx in flatten_idx])

foo = Solution()
print(foo.convert("ABCDEFGHIJKLMN", 1) == "ABCDEFGHIJKLMN")
print(foo.convert("ABCDEFGHIJKLMN", 2) == "ACEGIKMBDFHJLN")
print(foo.convert("ABC", 2) == "ACB")
print(foo.convert("ABC", 3) == "ABC")
print(foo.convert("ABC", 9) == "ABC")
print(foo.convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR")

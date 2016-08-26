from solution import Solution

cases = [
    ([5, 7, 7, 8, 8, 10], 8, [3, 4]),
    ([1], 8, [-1, -1]),
    ([1], 1, [0, 0]),
    ([1, 1], 1, [0, 1]),
    ([0, 1], 1, [1, 1]),
    ([0, 2], 1, [-1, -1]),
    ([0, 0, 1, 1, 1, 4, 5, 5], 2, [-1, -1]),
    ([1, 2, 3], 3, [2, 2]),
    ([1, 2, 3], 1, [0, 0]),
]

for case in cases:
    rslt = Solution().searchRange(case[0], case[1])
    print rslt == case[2], rslt


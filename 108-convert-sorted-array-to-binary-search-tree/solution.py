# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def pre_order(self):
        rslt = []
        if self.left is not None:
            rslt.extend(self.left.pre_order())

        rslt.append(self)

        if self.right is not None:
            rslt.extend(self.right.pre_order())

        return rslt

    def __repr__(self):
        return str(self.val)

    def __str__(self):
        return str(self.val)


class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """

        return self.insertNode(nums)

    def insertNode(self, nums):
        list_len = len(nums)
        if list_len == 0:
            return

        if list_len == 1:
            return TreeNode(nums[0])

        mid_idx = int(list_len / 2)
        mid_node = TreeNode(nums[mid_idx])
        mid_node.left = self.insertNode(nums[:mid_idx])
        mid_node.right = self.insertNode(nums[mid_idx + 1:])
        return mid_node


foo = Solution()
print([n for n in foo.sortedArrayToBST(list(range(10))).pre_order()])



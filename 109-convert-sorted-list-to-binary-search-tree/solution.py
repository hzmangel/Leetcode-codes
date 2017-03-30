# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    @classmethod
    def buildFromArray(cls, nums):
        nodes = [ListNode(n) for n in nums]
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]

        return nodes[0]


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
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """

        return self.insertNode(head, None)

    def insertNode(self, head, tail):
        if head == tail:
            return
        slow = head
        fast = head

        while fast != tail and fast.next != tail:
            fast = fast.next.next
            slow = slow.next

        # After loop, slow should be middle of the list, then should be the root
        # of the tree
        root_node = TreeNode(slow.val)
        if head != slow:
            root_node.left = self.insertNode(head, slow)
        if slow.next != tail:
            root_node.right = self.insertNode(slow.next, tail)
        return root_node


foo = Solution()
foo.sortedListToBST(None)
test_set = ListNode.buildFromArray(range(10))
print(foo.sortedListToBST(test_set).pre_order())


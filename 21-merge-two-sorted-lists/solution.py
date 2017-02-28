# Definition for singly-linked list.
class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None

    def print_nodes(self):
        cursor = self
        while(cursor):
            print(cursor.val)
            cursor = cursor.next


class Solution(object):

    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        curr_node = None
        prev_node = None
        head = None

        while(l1 and l2):
            if l1.val >= l2.val:
                curr_node = ListNode(l2.val)
                l2 = l2.next
            else:
                curr_node = ListNode(l1.val)
                l1 = l1.next

            if prev_node:
                prev_node.next = curr_node
                prev_node = curr_node
            else:
                head = curr_node
                prev_node = head

        while(l1):
            curr_node = ListNode(l1.val)
            if prev_node:
                prev_node.next = curr_node
                prev_node = curr_node
            else:
                head = curr_node
                prev_node = head

            l1 = l1.next

        while(l2):
            curr_node = ListNode(l2.val)
            if prev_node:
                prev_node.next = curr_node
                prev_node = curr_node
            else:
                head = curr_node
                prev_node = head

            l2 = l2.next

        return head


foo = Solution()
l1 = [ListNode(i) for i in range(0, 20, 2)]
for idx in range(len(l1) - 1):
    l1[idx].next = l1[idx + 1]
l2 = [ListNode(i) for i in range(1, 20, 2)]
for idx in range(len(l2) - 1):
    l2[idx].next = l2[idx + 1]

head = foo.mergeTwoLists(l1[0], l2[0])
head.print_nodes()

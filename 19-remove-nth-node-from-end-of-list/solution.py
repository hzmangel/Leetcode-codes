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

    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        if not head.next:
            return []

        cursor = head
        for i in range(n):
            cursor = cursor.next

        prev_cursor = None
        del_cursor = head

        while(cursor):
            prev_cursor = del_cursor
            del_cursor = del_cursor.next
            cursor = cursor.next

        if not prev_cursor:  # No prev cursor, del cursor is head
            return del_cursor.next
        else:
            prev_cursor.next = del_cursor.next

        return head

foo = Solution()
total_cnt = 2
linked_list = [ListNode(i) for i in range(total_cnt)]
for i in range(total_cnt - 1):
    linked_list[i].next = linked_list[i + 1]

linked_list[0].print_nodes()
foo.removeNthFromEnd(linked_list[0], 1)
linked_list[0].print_nodes()

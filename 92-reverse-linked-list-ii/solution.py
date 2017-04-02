# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    @classmethod
    def genList(cls, nums):
        nodes = [ListNode(n) for n in nums]
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]

        return nodes[0]

    def __repr__(self):
        return str(self.val)


class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """

        if m == n:
            # No element requires reverse
            return head

        pre = head
        reverse_head = head
        for _ in range(m - 1):
            pre = reverse_head
            reverse_head = reverse_head.next

        if reverse_head.next is None:
            return head

        reverse_tail = reverse_head
        for _ in range(n - m):
            reverse_tail = reverse_tail.next

        # reverse head is first element, create a fake head node for pre
        if reverse_head == head:
            pre = ListNode(None)
            pre.next = head

        curr = reverse_head
        curr_end = reverse_tail
        while curr != reverse_tail:
            next_iter = curr.next

            pre.next = next_iter
            curr.next = curr_end.next
            curr_end.next = curr

            curr = next_iter


        if reverse_head == head:
            return pre.next
        else:
            return head


foo = Solution()
head = ListNode.genList([1,2,3,4,5,6])
p = foo.reverseBetween(head, 1, 5)
while p is not None:
    print(p.val,)
    p = p.next



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

    def __repr__(self):
        rslt = []
        head = self
        while head is not None:
            rslt.append(str(head.val))
            head = head.next

        return ','.join(rslt)


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head

        prev = None
        curr = head
        new_head = curr.next

        # This is the previous wrong code
        # while curr.next is not None and curr.next.next is not None:
        # Error: Checking next and next.next causes the last two elements not be
        # swapped.
        # Failed case: [2, 1]

        while curr is not None and curr.next is not None:
            next_curr = curr.next.next
            if prev is not None:
                prev.next = curr.next

            curr.next.next = curr
            curr.next = next_curr
            prev = curr

            # Wait for next iteration
            curr = next_curr

        return new_head


foo = Solution()
test_set = ListNode.buildFromArray([1,2])
#test_set = ListNode.buildFromArray(range(10))
print(test_set)
print(foo.swapPairs(test_set))


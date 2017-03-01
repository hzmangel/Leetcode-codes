# Definition for singly-linked list.
class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None

    def print_nodes(self):
        cursor = self
        rslt = []
        while(cursor):
            rslt.append(cursor.val)
            cursor = cursor.next
        print(rslt)


def build_list(nums):
    l = [ListNode(i) for i in nums]
    for idx in range(len(l) - 1):
        l[idx].next = l[idx + 1]
    return l


class Solution(object):

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        rslt_head = None
        rslt_cursor = None
        heads = [l for l in lists if l]

        while(heads):
            min_node = heads[0]
            min_val = min_node.val
            min_idx = 0

            for idx, head_node in enumerate(heads[1:]):
                if head_node.val < min_val:
                    min_node = head_node
                    min_val = head_node.val
                    min_idx = idx + 1

            # print('-' * 20)
            # print(min_idx, min_val, heads[min_idx].val)
            if rslt_head:
                rslt_cursor.next = min_node
                rslt_cursor = rslt_cursor.next
            else:
                rslt_head = min_node
                rslt_cursor = rslt_head

            heads[min_idx] = heads[min_idx].next
            if not heads[min_idx]:
                heads.pop(min_idx)

        return rslt_head


foo = Solution()
l1 = build_list(range(0, 20, 3))
l2 = build_list(range(1, 20, 4))
l3 = build_list(range(2))

head = foo.mergeKLists([l1[0], l2[0], l3[0], None])
head.print_nodes()

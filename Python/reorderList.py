import collections

from utils import create_linked_list, linked_to_list, ListNode


class Solution:
    def reorderList(self, head: ListNode) -> ListNode:
        """
        O(n) time
        O(1) space
        :param head:
        :return:
        """

        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = self.reverse(slow.next)
        slow.next = None

        first, second = head, prev
        while second:
            fb, sb = first.next, second.next
            first.next = second
            second.next = fb
            first, second = fb, sb

        return head  # problem said dont do this

    def reverse(self, head: ListNode):
        """
        O(n) time
        O(1) space
        :param head:
        :return:
        """
        if head is None:
            return head
        prior = None
        while head.next is not None:
            next = head.next
            head.next = prior
            prior = head
            head = next
        head.next = prior
        return head


if __name__ == "__main__":
    head = [1, 2, 3, 4, 5]
    head = create_linked_list(head)
    ans = [1, 5, 2, 4, 3]
    resp = Solution().reorderList(head)
    resp = linked_to_list(resp)
    if ans == resp:
        print("PASS", resp)
    else:
        print("FAIL", resp)

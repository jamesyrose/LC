import collections

from utils import create_linked_list, linked_to_list, ListNode


class Solution:
    def mergeTwoLists(self, head: ListNode, n: int) -> ListNode:
        """
        O(k) time where k is len(head)
        O(k) space wehre k is len(head)

        :param head:
        :param n:
        :return:
        """

        mem = collections.deque(maxlen = n)
        newHeadBuff = newHead = ListNode()
        while head:
            if len(mem) == n:
                newHead.next = mem.popleft()
                newHead = newHead.next
            mem.append(head)
            head = head.next
        mem.popleft()
        for i in range(len(mem)):
            newHead.next = mem.popleft()
            newHead = newHead.next
        newHead.next = None
        return newHeadBuff.next

    def mergeTwoLists2(self, head: ListNode, n: int) -> ListNode:
        """
        O(k) time where k is len(head)
        O(k) space wehre k is len(head)

        :param head:
        :param n:
        :return:
        """
        newHead = ListNode(0)
        newHead.next = head
        l, r = newHead, head
        while n > 0 and r:
            r = r.next
            n -= 1
        while r:
            l = l.next
            r = r.next
        l.next = l.next.next
        return newHead.next








if __name__ == "__main__":
    l1 = [1]
    n = 1
    head = create_linked_list(l1)
    ans = [1, 2,3,5]
    resp = Solution().mergeTwoLists2(head, n)
    resp = linked_to_list(resp)
    if ans == resp:
        print("PASS", resp)
    else:
        print("FAIL", resp)

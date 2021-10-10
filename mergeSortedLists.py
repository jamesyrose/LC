from utils import create_linked_list, linked_to_list, ListNode


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        O(n + m)  time
        O(n + m) space

        :param l1:
        :param l2:
        :return:
        """
        if l1 is None:
            return l2
        elif l2 is None:
            return l1

        head = newHead = ListNode()

        while l1 and l2:
            if l1.val < l2.val:
                newHead.next = l1
                l1 = l1.next
            else:
                newHead.next = l2
                l2 = l2.next

            newHead = newHead.next
        if l1:
            newHead.next = l1
        elif l2:
            newHead.next = l2
        return head.next


if __name__ == "__main__":
    l1 = [1, 2, 4]
    l2 = [1, 3, 4]
    l1 = create_linked_list(l1)
    l2 = create_linked_list(l2)
    ans = [1, 1, 2, 3, 4, 4]
    resp = Solution().mergeTwoLists(l1, l2)
    resp = linked_to_list(resp)
    if ans == resp:
        print("PASS", resp)
    else:
        print("FAIL", resp)

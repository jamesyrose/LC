from utils import create_linked_list, linked_to_list, ListNode


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        """
        O(n) time
        O(n) space

        :param head:
        :return:
        """
        if not head:
            return False
        checked = set()
        while head.next:
            checked.add(head)
            if head.next in checked:
                return True
            head = head.next
        return False

    def hasCycle2(self, head: ListNode) -> bool:
        """
        O(n) time
        O(1) space

        Toutoise and hare
        :param head:
        :return:
        """
        if not head:
            return False
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


if __name__ == "__main__":
    temp = [3, 2, 0, -4]
    head = create_linked_list(temp)
    ans = True
    resp = Solution().hasCycle(head)
    if ans == resp:
        print("PASS", resp)
    else:
        print("FAIL", resp)

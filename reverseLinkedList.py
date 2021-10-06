from utils import create_linked_list, linked_to_list, ListNode


class Solution:
    def reverse(self, head: ListNode):
        prior = None
        while head.next is not None:
            next = head.next
            head.next = prior
            prior = head
            head = next
        head.next = prior
        return head


if __name__ == "__main__":
    temp = [1, 2, 3, 4, 5, 6, 7, 8]
    head = create_linked_list(temp)
    ans = [8, 7, 6, 5, 4, 3, 2, 1]
    resp = Solution().reverse(head)
    resp = linked_to_list(resp)
    if ans == resp:
        print("PASS", resp)
    else:
        print("FAIL", resp)

from utils import create_linked_list, linked_to_list, ListNode


class Solution:
    def mergeKLists(self, lists: list) -> ListNode:
        """
        O(log k) time

        where n = sum(listNode)
        :param lists:
        :return:
        """
        if not lists or len(lists) == 0 :
            return None

        while len(lists) > 1:
            merged = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                if i + 1 < len(lists):
                    l2 = lists[i + 1]
                else:
                    l2 = None
                merged.append(self.mergeTwoLists(l1, l2))
            lists = merged
        return lists[0]

    def mergeKLists2(self, lists: list) -> ListNode:
        """
        O(n log k) time
        :param lists:
        :return:
        """
        lists = [h for h in lists if h] # remove nones
        if len(lists) == 1:
            if lists[0]:
                return lists[0]
            else:
                return None
        if len(lists) == 0:
            return None
        head = newHead = ListNode()

        while len(lists) > 1:
            # find the min val
            val_lists = [node.val for node in lists]
            min_idx = val_lists.index(min(val_lists))
            # get the linked list
            next_head = lists[min_idx]
            # set the next to head of min linked list
            newHead.next = next_head
            if next_head.next:
                lists[min_idx] = next_head.next # iterate the head up
            else:
                lists.pop(min_idx)
            newHead = newHead.next # move new head up

        newHead.next = lists[0]

        return head.next
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
    lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
    lists = [create_linked_list(a) for a in lists]
    ans = [1, 1, 2, 3, 4, 4, 5, 6]
    resp = Solution().mergeKLists(lists)
    resp = linked_to_list(resp)
    if ans == resp:
        print("PASS", resp)
    else:
        print("FAIL", resp)

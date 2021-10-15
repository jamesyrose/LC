from collections import deque
class ListNode:
   def __init__(self, val = None):
      self.val = val
      self.next = None

def create_linked_list(l: list, singly = True):
   head = temp = ListNode(l[0])
   for n in l[1:]:
      head.next = ListNode(n)
      head = head.next
   if singly:
      head = temp
      return head
   else:
      head.next = temp
      head = temp
      return head


def linked_to_list(head: ListNode):
   vals = [head.val]
   while head.next is not None:
      head = head.next
      vals.append(head.val)
   return  vals


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(sequence):
   # Create a list of trees
   forest = [TreeNode(x) for x in sequence]

   # Fix up the left- and right links
   count = len(forest)
   for index, tree in enumerate(forest):
      left_index = 2 * index + 1
      if left_index < count:
         tree.left = forest[left_index]

      right_index = 2 * index + 2
      if right_index < count:
         tree.right = forest[right_index]

   return forest[0]  # root

def tree_to_list(seq):
   res = []
   queue = deque([seq])
   while queue:
      for i in range(len(queue)):
         node = queue.popleft()
         if node:
            res.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
   return res











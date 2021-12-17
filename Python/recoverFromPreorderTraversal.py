# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        """
        O(n) time
        """
        vals = re.findall('\d+|-+', traversal)
        vals = collections.deque(vals)

        head = TreeNode(vals.popleft())

        def dfs(curr, lvl):  # O(v) time where v is the number of nodes
            for _ in range(2):
                if len(vals) == 0:
                    return
                level = len(vals[0])
                if lvl + 1 == level:
                    l = len(vals.popleft())
                    v = int(vals.popleft())
                    if not curr.left:
                        curr.left = TreeNode(v)
                        dfs(curr.left, l)
                    else:
                        curr.right = TreeNode(v)
                        dfs(curr.right, l)

        dfs(head, 0)
        return head

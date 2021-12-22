# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        """
        O(n) where n is number of nodes
        :param root:
        :param targetSum:
        :return:
        """
        if not root:
            return []
        res = []

        def dfs(node, path, curr_sum):
            path.append(node.val)
            curr_sum += node.val
            if not node.left and not node.right:
                # leaf node
                if curr_sum == targetSum:
                    res.append(path[:])
                path.pop()
                curr_sum -= node.val
                return
            if node.right:
                dfs(node.right, path, curr_sum)
            if node.left:
                dfs(node.left, path, curr_sum)
            path.pop()
            curr_sum -= node.val

        dfs(root, [], 0)
        return res



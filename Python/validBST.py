import collections

from utils import TreeNode, build_tree, tree_to_list


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        """
        O(n) time and space for DFS
        :param root:
        :return:
        """
        return self.valid(root, -2 ** 32, 2 ** 32)

    def valid(self, root, min_val, max_val):
        if not root or root.val is None:
            return True
        if root.val >= max_val or root.val <= min_val:
            return False
        l = True
        r = True
        # print(root.val, root.left.val, root.right.val)
        if root.left and root.left.val is not None:
            l = self.valid(root.left, min_val, min(max_val, root.val))
        if root.right and root.right.val is not None:
            r = self.valid(root.right, max(min_val, root.val), max_val)
        return (l and r)


if __name__ == "__main__":
    null = None
    test_case = [
        [2, 2, 2],
        [-2147483648]
    ]
    for test in test_case:
        root = build_tree(test)

        ans = False
        resp = Solution().isValidBST(root)
        if ans == resp:
            print("PASS", resp, "-" * 10)
        else:
            print("FAIL", resp, "-" * 10)

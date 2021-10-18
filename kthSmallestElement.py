import collections

from utils import TreeNode, build_tree, tree_to_list


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        """
        In Order DFS
        O(n) time and space

        :param root:
        :param k:
        :return:
        """
        def dfs(node):
            if not node or node.val is None:
                return
            dfs.stack.append(node)
            if node.left and node.left.val is not None:
                dfs(node.left)
                dfs.arr.append(node.val)
            else:
                dfs.arr.append(node.val)
            dfs(node.right)

        dfs.stack = []
        dfs.arr = []
        dfs(root)
        return dfs.arr[k-1]

    def kthSmallest2(self, root: TreeNode, k: int) -> int:
        """
        O(n log n) for sorted function
        DFS is O(n) time and space

        :param root:
        :param k:
        :return:
        """
        def dfs(node):
            if not node or node.val is None:
                return
            dfs.arr.append(node.val)
            dfs(node.right)
            dfs(node.left)
            return

        dfs.arr = []
        dfs(root)
        return sorted(dfs.arr)[k-1]


if __name__ == "__main__":
    null = None
    test_case = [
        [[3, 1, 4, null, 2], 1],
        [[5, 3, 6, 2, 4, null, null, 1], 3]
    ]
    for test in test_case:
        root = build_tree(test[0])

        ans = False
        resp = Solution().kthSmallest(root, test[1])
        if ans == resp:
            print("PASS", resp, "-" * 10)
        else:
            print("FAIL", resp, "-" * 10)
